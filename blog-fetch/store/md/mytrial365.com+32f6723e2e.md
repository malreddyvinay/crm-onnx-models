Opening Hook Imagine a customer raises a support ticket. "Our Power Automate flow is suddenly slow." As developers, our instinct is usually to open the flow designer. Sometimes one of those fixes works. Most of the time... We are fixing the wrong thing. Because we don't actually understand what happens after a flow is triggered. … Continue reading The Journey of a Single Request

# There Is No Such Thing as “The Power Platform API Limit”

Every few months I see another discussion where someone says: "Dataverse API limit is 6000." "No, it's 40,000 requests." "Actually it's 250,000." "Power Automate allows 500,000." Everyone sounds correct. Yet everyone is talking about a completely different limit. That is exactly why Power Platform limits are so confusing. Microsoft hasn't created one limit. They have … Continue reading There Is No Such Thing as “The Power Platform API Limit”

# Designing Searchable Experiences: Mastering the Quick Find View

"A search engine is only as good as the information it has been told to search." In the previous article, we explored how administrators decide which tables participate in the Dataverse Search Index. We learned that not every table belongs in the search index, and that careful planning is essential for building a scalable and … Continue reading Designing Searchable Experiences: Mastering the Quick Find View

# Designing Searchable Tables: A Deep Dive into the Dataverse Search Index

In the previous articles, we explored the search-related settings available in the Power Platform Admin Center and learned how Search Indexing, Global Search, Quick Find, and Microsoft 365 integration work together to deliver a modern search experience. Now we arrive at one of the most important questions in the entire series: How does Dataverse decide … Continue reading Designing Searchable Tables: A Deep Dive into the Dataverse Search Index

# Optimising Dataverse Search: Understanding the Search Settings in Power Platform

"Enabling Dataverse Search is only the beginning. The real user experience is shaped by how you configure the search behaviour." In the previous article, we explored the Dataverse Search section in the Power Platform Admin Center and learned how Search Indexing, the Global Search Bar, and Search-Only Experiences work together to build the foundation for … Continue reading Optimising Dataverse Search: Understanding the Search Settings in Power Platform

# Building the Foundation: Understanding Dataverse Search Configuration

"Search isn't just a feature anymore it's becoming the foundation for AI, Copilot, and intelligent experiences across Microsoft Power Platform." Throughout this series, we have explored how Dataverse Search works behind the scenes from search indexing and relevance ranking to facets, filters, and the search pipeline. But before any of that can happen, there is … Continue reading Building the Foundation: Understanding Dataverse Search Configuration

# Why This Record Appears First: Understanding Relevance Ranking, Facets, and Filters in Dataverse Search

In the previous article, we explored how Dataverse prepares searchable information behind the scenes so users can search across multiple tables almost instantly. But another question naturally follows: When several records match my search, why does one appear at the top while another appears further down the list? The answer lies in relevance ranking, along … Continue reading Why This Record Appears First: Understanding Relevance Ranking, Facets, and Filters in Dataverse Search

# Designing for Search: How Dataverse Decides What Gets Indexed

In the previous articles, we discovered that Dataverse Search doesn't scan your database every time someone performs a search. Instead, it searches a dedicated search index that is maintained in the background. That naturally leads to another question: How does Dataverse decide what actually goes into that index? Does every table get indexed? Does every … Continue reading Designing for Search: How Dataverse Decides What Gets Indexed

# Dataverse Search vs Quick Find vs Advanced Find – Choosing the Right Search for the Right Job

By now, we have uncovered two important truths about Dataverse Search. First, it doesn't search the database directly. Second, it relies on a dedicated search index that is continuously maintained in the background. But if Dataverse Search is so powerful, why do Quick Find and Advanced Find still exist? It's a question many developers ask … Continue reading Dataverse Search vs Quick Find vs Advanced Find – Choosing the Right Search for the Right Job

# The Hidden Search Index That Makes Everything Fast

In the first article, we learned something that surprises many Power Platform developers: Dataverse Search doesn't search your tables directly. Instead, it searches something called a search index. That naturally raises the next question: If users aren't searching the database, where do the search results actually come from? The answer lies in one of the … Continue reading The Hidden Search Index That Makes Everything Fast