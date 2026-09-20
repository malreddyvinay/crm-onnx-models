When working with Power Platform, the Dev environment often holds the latest version of what your team is building. However, tracking what actually changed between exports across components, flows, and configurations is a tedious task. The diffs are noisy, the XML is unreadable, and manual review doesn't scale. Here's how I used GitHub Actions and … Continue reading AI-Powered Summaries for Power Platform Solution Changes with GitHub Actions

# Inside KingswaySoft’s Dataverse Destination – Optional Settings: What You Need to Know

Today, we will learn how the Optional Setting features in KingswaySoft translate into HTTP Request-Response (with the help of Fiddler). The purpose of this document is to describe system behavior, to prevent performance degradation, and to support effective feature utilization. Enjoy! Data Flow Setup For demo purposes, I created a simple Excel to be ingested … Continue reading Inside KingswaySoft’s Dataverse Destination – Optional Settings: What You Need to Know

# Fixed Dataverse AI Prompt Columns Error: Principal user … is missing prvReadmsdyn_AIModel

The preview feature of Dataverse AI Prompt Columns enables us to tie specific Dataverse columns and add generative AI capabilities to be used in Apps, Workflows, or Reports. For example, we can add sentiment analysis to a specific column of the Case table/entity, or you can also ask for translation or even generate a structured … Continue reading Fixed Dataverse AI Prompt Columns Error: Principal user … is missing prvReadmsdyn_AIModel

# Dataverse: Avoiding Timezone Pitfalls When Integrating Dataverse Date and DateTime Fields

New day, new things to learn. While integrating with Dataverse may seem straightforward at first, especially when it comes to DateTime things, it can quickly become complex due to different configuration settings. In this post, I’ll walk through the key factors that cause these variations, so you can confidently choose the right settings before building … Continue reading Dataverse: Avoiding Timezone Pitfalls When Integrating Dataverse Date and DateTime Fields

# Dataverse: Retrieve unmasked data (Masking Rule Column) via KingswaySoft

New day, new experience to discover! This time, I have a requirement to create an SSIS batch job function. During data retrieval, I found that the column is masked using the Masking Rule. This blog post is a brief note on how to retrieve the unmasked data. Enjoy! Dataverse Column Security Profile First, we need … Continue reading Dataverse: Retrieve unmasked data (Masking Rule Column) via KingswaySoft

# Dataverse: Avoid Concurrency issues by using Azure Service Bus Queue and Azure Functions

Another blog post to handle the concurrency issue. Previously, I shared how to do concurrency via a plugin in this blog post and also how to force concurrency behavior in Dataverse in this post. However, when I attempted to implement this, it still did not resolve the concurrency issues, as the platform itself, I believe, … Continue reading Dataverse: Avoid Concurrency issues by using Azure Service Bus Queue and Azure Functions

# Dataverse: How to set a Complex Query for System View

Sometimes, we need to let the user see only the records under their care (dynamically connected via relationships). For example, we have the Region table > User and Order will be linked to the Region. Hence, the user will only see all the Order records that belong to the same Region as the User's Region. … Continue reading Dataverse: How to set a Complex Query for System View

# Azure Function to scrape Yahoo data and store it in SharePoint

A couple of weeks ago, I learned about an AI Agent from this Microsoft DevBlogs, which mainly talks about building an AI Agent on top of Copilot Studio. So, as a good student, I tried to build my own Agent to learn about Indonesian Stocks. But, for this part, I just want to show the … Continue reading Azure Function to scrape Yahoo data and store it in SharePoint

# Dataverse: Get best Threads and Rows Count

To know the best settings for pushing data to Dataverse is tedious work (for batch processing). We need to consider the client hardware (Logical processor - to support multithreading and ram capacity), Network, and also it is unique for each of the tables that you want to run (for the Plugins/Workflow/Power Automate that trigger afterwards). … Continue reading Dataverse: Get best Threads and Rows Count

# What I learned about SSIS

Happy New Year, everyone! Today, I want to share a list of knowledge that I have gained since I started learning SSIS - KingswaySoft! Certainly, the tips I wrote here may not be applicable/outdated later on, and you can call them out or discuss with me if you think I have a wrong understanding. Without … Continue reading What I learned about SSIS