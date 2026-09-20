## Low-Code & Pro-Code together: Create CSV file with PA and Custom API

Low-code is advancing fast with each Power Platform release, but pairing it with pro-code truly unlocks its potential. In a recent project, I needed a solution to retrieve records and generate a CSV from a Dataverse view with thousands of records.

Using Power Automate with a Custom API, I optimized performance by processing records in 250-record batches, ensuring both speed and reliability within API limits.

## Low-code & Pro-code working together: Hierarchical view in Canvas App

In this post, I explore how low-code and pro-code approaches can work together to create a hierarchical view in Power Apps Canvas Apps. Drawing inspiration from a previous solution I developed for Model-Driven Apps using a PCF, I wanted to see if a similar feature could be implemented using Canvas Apps. By leveraging a custom API to prepare data in a hierarchical structure on the server side, and combining it with Power Fx for minimal code on the client side, I demonstrate how to efficiently render hierarchical data in a Canvas App. This method reduces the complexity of Power Fx code while maintaining a rich user experience. Special thanks to Tiran Dagan for the inspiration.

## Power Platform 2024 release wave 2

The 2024 Wave 2 release for Power Platform brings significant enhancements, including the ability to restore deleted records, integrate Dataverse with Microsoft Fabric for advanced data analysis, and use AI-powered copilots in Teams. Additional features include image processing with GPT-4 Vision, Power Fx integration in web templates. These updates streamline processes, boost productivity, and enhance collaboration.

## Dataverse REST Builder and the Hidden Gems

The Dataverse REST Builder, a crucial tool in XRMToolbox, enables creating and executing requests against the Dataverse Web API endpoint, invaluable for consultants who need to call Custom APIs from various parts of the platform, such as ribbon buttons. To use it, you connect to your environment, create a new collection and request, select the Custom API

## From Basics to Brilliance: TypeScript Examples for Model Driven Apps

Unleash the power of TypeScript in Model Driven Apps! Explore practical examples, from handling basic logic in main forms to opening Custom Pages, calling Custom APIs, and triggering Cloud Flows. Ready-to-use code for your projects – tweak it according to your needs! Dive into the details and elevate your app development game

## How to create a TypeScript project for Model Driven Apps

This is the continuation of a series on how to apply TypeScript in Model Driven Apps, In my previous blog post I’ve explained what TypeScript is, pros and cons and how it helps in Model Driven Apps, in this case I’m going to walk you through on how to create a TypeScript project from scratch for Model Driven Apps.

 I will show you how to add the config files and one first example of TypeScript that you can apply to a main form, but don’t worry in my next blog post I will show you more cool examples

## What is TypeScript, pros and cons and how it helps in Model Driven Apps

In the quest for a fresh start this year, I’m going to create a series of blogposts that is a guide about TypeScript applied to Model Driven apps, inspired by my friend Ben den Blanken. Exploring TypeScript from the basics to practical examples, this first blogposts tries to explain the basics like what TypeScript is, its benefits and how it can help you in a Dataverse or Power Platform project.

## Import Excel file using Custom API and Alternate keys

Have you ever had headaches trying to build an integration using an Excel file?

If so, let me walk you through this blogpost where I’ve been trying to combine some tools to import an Excel file using Power Automate, but in a much more efficient way than using just the Excel connector.

In this solution I am using a cloud flow, a custom API and alternative keys to create a bulk Upsert request.

## Speed up your development process with GitHub Copilot

Are you ready to take your development experience to a whole new level? GitHub Copilot is your ultimate development companion, designed to boost your development process and increase your productivity. In this blogpost, I’ll walk you through every aspect of GitHub Copilot, from installation and configuration to creating an Azure Function connected to Dataverse that demonstrate how Copilot Works.

## Power Happening building highlights

Power Happening solution is live, this solution is about a Model Driven App that helps you to organize your community events. Together with my friend Ben den Blanken, we spent our free time over the last few months building this solution.

Therefore I’d like to share our findings building it and leveraging Scott’s PCF to deliver a drag & drop experience

## Power Platform Release wave 1 2023

It’s here, the release of wave 1 2023 was announced. Every year Microsoft delights us twice with the wave of releases so this time I wanted to share my list of top features about Power Platform I hope you enjoy it as much as I did reading it.

## Create a twin record with its children using a table relationship and field mapping

You have probably leverage of the field mapping functionality at some point, to copy fields from table A into a new record in table B. But what happens when you have a scenario like the following one: Copy fields from table A.1 (Child table of table A) into table B.1 (Child table of table B).

For this scenarios you have a hidden gem like the InitializeFromRequest class that you can use in a plugin or in a Custom API. let me walk you through this blogpost and show you how this can be done leveraging the out of the box features like table relationship and field mapping.