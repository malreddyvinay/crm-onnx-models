Within a Model Driven App there’s frequently a requirement to filter the values in a lookup field dynamically. To do this we can use the addPreSearch() method in the Client API. Let’s see how this interacts with the recently documented ’exists’/‘any’ FetchXml functionality.

On 27th March 2023 the solution checker was updated to include the warnings and errors output by the Flow Checker. Let’s investigate the flow checker warning ‘Actions in this flow may result in an infinite on trigger loop. Please ensure you add appropriate conditional checks to prevent this flow from triggering itself.’ (flow-avoid-recursive-loop).

What does it mean? How can one resolve the warning, especially when working with Dataverse? Let’s investigate.

With the release of Dependent Assemblies (preview) we can now use 3rd party libraries directly within plugins without the need for questionable ILMerge hacks. Lets use this to expand on the previous blog, Using Power Fx in Cloud Flows, so that we can more simply use Power Fx within a cloud flow.

In March 2021 Microsoft introduced Power Fx as “the low-code language that will be used across the Microsoft Power Platform”. Power Fx is currently used by Canvas Apps and Custom Pages but at Build 2021 Microsoft stated that Power Fx will be extended to Power Automate in the fullness of time. Wouldn’t it be interesting if we could use Power Fx within cloud flows today? Let’s explore how we can achieve this goal.

Bulk Delete has been around since the early days of Dynamics 365. The classic bulk delete interface has a number of limitations. Let’s see if we can use Power Automate to improve on the classic bulk delete.

The threepreviousposts in this series have examined how to obtain a list of deprecated actions in connectors, so that we can consider migrating to an updated action or alternative connector. In this post I will demonstrate a script that checks power platform solutions for deprecated actions.

In the last blog we created a durable function and custom connector and used them in a Power Automate Cloud Flow. In this blog, we’re going to update the Azure function to simplify its use within Power Automate - allowing us to use Power Automate’s normal output and error handling.

As the connector ecosystem matures some actions within connectors and perhaps even whole connectors are being deprecated. To avoid unexpected failures it’s useful to know when a connector or action is deprecated so that one can take action, such as migrating to an updated or alternate connector. This first post in a series of blog posts explains how to detect connectors or actions that have been deprecated using an Azure Durable Function and a Power Automate Custom Connector. We’ll extend this in later blog posts to make it more usable.