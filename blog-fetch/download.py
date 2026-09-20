import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import urlparse
import requests
import trafilatura

SCRIPT_DIR = Path(__file__).resolve().parent
SEED_FILE = SCRIPT_DIR / "seed_links.txt"
RAW_DIR = SCRIPT_DIR / "store" / "raw"
MD_DIR = SCRIPT_DIR / "store" / "md"
INDEX_FILE = SCRIPT_DIR / "store" / "index.jsonl"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def generate_slug(url: str) -> str:
    domain = urlparse(url).netloc.replace("www.", "")
    clean_domain = re.sub(r'[^\w\.-]', '_', domain)
    sha1_hash = hashlib.sha1(url.encode('utf-8')).hexdigest()[:10]
    return f"{clean_domain}+{sha1_hash}"

def write_index_record(record: dict):
    with open(INDEX_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")

def main():
    parser = argparse.ArgumentParser(description="Fetch and extract blog posts.")
    parser.add_argument("--limit", type=int, default=None, help="Limit total URLs to process for testing.")
    parser.add_argument("--refetch", action="store_true", help="Override and refetch existing files.")
    args = parser.parse_args()

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    MD_DIR.mkdir(parents=True, exist_ok=True)

    if not SEED_FILE.exists():
        print(f"Error: {SEED_FILE} not found.")
        return

    with open(SEED_FILE, "r", encoding="utf-8-sig") as f:
        lines = [line.strip() for line in f if line.strip()]

    urls_to_process = []
    seen = set()

    for url in lines:
        if not url.startswith(("http://", "https://")):
            continue
        
        if url in seen:
            continue
        seen.add(url)

        if "linkedin.com" in url or "chatgpt.com/canvas" in url:
            print(f"[SKIPPED] Filtered domain: {url}")
            continue

        urls_to_process.append(url)

    if args.limit:
        urls_to_process = urls_to_process[:args.limit]

    total = len(urls_to_process)
    print(f"Starting execution for {total} URLs...\n")

    for idx, url in enumerate(urls_to_process, 1):
        slug = generate_slug(url)
        raw_path = RAW_DIR / f"{slug}.html"
        md_path = MD_DIR / f"{slug}.md"
        domain = urlparse(url).netloc.replace("www.", "")

        if raw_path.exists() and not args.refetch:
            print(f"[{idx}/{total}] [EXISTS] Skipping {url}")
            continue

        try:
            response = requests.get(url, headers=HEADERS, timeout=25, allow_redirects=True)
            status_code = response.status_code
            html_content = response.text

            if status_code != 200:
                print(f"[{idx}/{total}] [BLOCKED/ERROR {status_code}] {url}")
                record = {
                    "slug": slug,
                    "url": url,
                    "domain": domain,
                    "title": "",
                    "status": status_code,
                    "byte_counts": {"html": 0, "md": 0}
                }
                write_index_record(record)
                continue

            with open(raw_path, "w", encoding="utf-8") as f:
                f.write(html_content)

            extracted_md = trafilatura.extract(
                html_content,
                url=url,
                output_format="markdown",
                include_tables=True
            ) or ""

            with open(md_path, "w", encoding="utf-8") as f:
                f.write(extracted_md)

            metadata = trafilatura.extract_metadata(html_content, url=url)
            title = metadata.title if metadata and metadata.title else ""

            html_bytes = len(html_content.encode("utf-8"))
            md_bytes = len(extracted_md.encode("utf-8"))

            record = {
                "slug": slug,
                "url": url,
                "domain": domain,
                "title": title,
                "status": status_code,
                "byte_counts": {
                    "html": html_bytes,
                    "md": md_bytes
                }
            }
            write_index_record(record)

            print(f"[{idx}/{total}] [200 OK] {url} -> {slug}")

        except Exception as e:
            print(f"[{idx}/{total}] [FAILED] {url} - Error: {e}")

    print("\nProcessing complete.")

if __name__ == "__main__":
    main()
