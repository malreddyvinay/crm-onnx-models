### Looking for something in particular?

# UPDATED: Form Submission and Event Registration Summaries in Customer Insights - Journeys

Struggling to use form submission and event registration data in Customer Insights – Journeys? Learn how to automate readable and JSON structured summaries with Power Automate, including custom fields and consent!

# Customise Double Opt-In Confirmation Email {{OptedInPurposeTopic}} - Customer Insights - Journeys

If you are struggling with the unformatted, semicolon-separated list of selected topics and purposes from {{OptedInPurposeTopic}} in your double opt-in emails, this guide shows how to present them as a clean, bulleted list instead.

By extending the Field Submission table with additional columns, using Power Automate to extract field values, and some minor updates to the DOI Email and Journey, you can create a clear, structured, and professional double opt-in confirmation email experience.

# Trigger a flow when a Power Automate Approval is complete (Accepted or Rejected)

Stop waiting on approvals—trigger a flow the moment a decision is made


The post shows how to trigger a Power Automate flow when an Power Automate Approval is completed (instead of using “Wait for approval”). A more reliable, scalable way to integrate approvals into apps and business processes. It uses Dataverse triggers on the Approval table to detect completion, then retrieves the response, comments, and approver, links it back to the original row via the Approval ID, and updates that row with the outcome.

# Respond to a Power Automate Flow Approval in a Power Apps Custom Page or Canvas App

How to respond to Power Automate approval requests directly within a Power Apps custom page or canvas app, rather than email buttons or in Microsoft Teams. By capturing the Approval ID when creating an approval and storing it in Dataverse, you can retrieve, display, and act on approval requests inside your app experience.

This app-driven method gives you much greater control over the user experience, enabling custom UI, validation (like mandatory comments), and tighter integration with Dynamics 365. It also opens the door to richer scenarios such as surfacing approval history, triggering downstream automations, and embedding approvals seamlessly into model-driven or canvas app workflows.

# Unique Join Link for Teams Meetings and Webinars in Dynamics 365 Customer Insights - Journeys

Dynamics 365 Customer Insights – Journeys integrates with Microsoft Teams to enable attendee‑level tracking through unique join links for meetings and webinars. While the standard approach uses the built‑in Join in Teams button in journey emails, this isn’t always reliable when emails need to be resent or shared through other channels. This post shows how those unique join links are constructed behind the scenes and how to use a PowerFX calculated column on the Event Registration table to automatically generate a Teams join URL per registrant which works seamlessly across environments and ensures every attendee check‑in is accurately captured in Dynamics—without manual effort or error‑prone processes.

# ReCAPTCHA V3 and Cloudflare Turnstile for Customer Insights - Journeys Forms

How to implement Google ReCAPTCHA v3 or Cloudflare Turnstile for Customer Insights - Journeys marketing or event forms with minimal form configuration and code wresting!

# Change the appearance of Marketing and Event forms using URL parameters in Customer Insights - Journeys

How to change the appearance of a Customer Insights - Journeys form based on URL parameters, for when you want to (or have to) use the same form for different personas, brands or behaviours.

For example, an event will only allow you to use one form for taking registrations, but you may want to change the form visuals based on the person invited. Using separate events would make it difficult to manage capacity, impossible to use streaming in teams and some very disjointed reporting. So lets make a single form work for both!

# Automated weekly product emails in Customer Insights - Journeys

How to automatically and dynamically generate email content in Customer Insights - Journeys using product data in Dataverse No power automate flows required here, only a delightfully configured Dataverse table, a Journey with branches, and an Email with conditional content/lists.

# Export exact copies of emails sent, including personalisation and conditional content, from Customer Insights - Journeys

This post will show you how to export the exact copies of emails from Dynamics 365 Customer Insights - Journeys using Power Automate with the new marketing email API. It takes the feature switch ‘*Show exact copy of sent emails*’ to the next level!

Why you might want to do this? Well I’m not here to sell it to you, but here are some suggestions as per the release notes:

- Maintaining accurate records of customer communications
- Legal compliance
- Resolving disputes
- Managing customer relationships
- Quality assurance
- Operational efficiency
- Data analysis

# Segments in Customer Insights - Journeys: Bulk delete with Power Automate

Currently its not possible to delete segments more than one at a time from the view in Dynamics 365 Customer Insights - Journeys. Why? I don’t know. Why do you need to? That’s up to you, but it’s a question I have been asked often. And I love an excuse to go digging into these things. There is no way via the UI or bulk delete, but you can use a flow (or other automation tool that makes API calls) to do this.

P.S With great power comes great responsibility and don’t blame me if you delete the wrong things!

# Marketing to Leads and Contacts without duplicate sends in Customer Insights - Journeys

How can I send a marketing email to a segment of Leads and Contacts without sending an email to the same email address twice?


Journeys and segments must be Lead **or** Contact based but they could share the same email address and sending duplicate emails to the same email address isn’t cool. This post will show you how to exclude or include segment members with a list of email addresses.

# Event Waitlist Journeys & Triggers

Event waitlists have arrived for Customer Insights - Journeys which means self service event cancellation and automated (or manual) registration of waitlisted registrations when slots become available. **BUT shiny new features also means changes in the way things work.**

We now have three different triggers to handle event registrations with the relevant communications. The ‘Marketing Event Registration Created’ trigger will only fire when a registration is created as ‘Registered’, so if someone joins a waitlist, then later a space becomes available for them to register - they **will not receive any of the communications** in the ‘Marketing Event Registration Created’ journey.

This post shows you how to update your journeys to make sure your registrations converted from waitlisted receive all the right communications.

# Event Registration Cancellation Form Styling in Customer Insights - Journeys

The much awaited ‘Event registration cancellation’ feature for Customer Insights - Journeys is here which means organizers and attendees cancel event registrations. This post will give you a little collection of tips customise and style the Cancellation Form to make it look a little bit more professional. It’s all easy CopyPasta™ so no coding knowledge is required!

# Reuse a Single Email for all your Event Invitations in Customer Insights - Journeys

How to use a trigger based journey to **send event invitations** to a segment of your choice, for any event. The invitation email content is automatically personalised with the correct details for your chosen event. No development or flows required, just a ‘Custom’ Trigger and a single journey/email.

# Create a Case or a Lead from a marketing form in Customer Insights - Journeys

Many websites have a generic ‘contact us’ form on their website which could serve a variety of purposes, some of these may be lead such as enquiries about products or a request for a quote. But it could also be something better handled by the customer service teams such as a problem with an purchase, feedback or complaints. These are definitely not leads but often come in via the same form.

This posts shows you how a single marketing form in Customer Insights Journeys can be used to create a Lead or Case according to the type of enquiry being submitted.

# Create Form Submission and Event Registration Summaries in Customer Insights - Journeys

Form submissions and event registrations for Customer Insights - Journeys capture important information that is often way harder to find than it should be. This post will show you how to create a flow which:

- Creates an easy to read free text summary for each form submission or event registration
- Creates a JSON summary that can be used to export form submissions and event registrations, and other cool automations

# Set ‘Regarding’ to any (eligible) table in single update action in Power Automate

A helpful little tip for working with the ‘Regarding’ column in Dataverse Activities & Notes with Power Automate. Setting the value of the ‘Regarding’ column for more than one specific table can be messy and unreliable. This will show you how to set regarding to any (eligible) table with a single property JSON that can use dynamics inputs from any table.

Some examples where I use this are generating a **note** or **email** notification (or any other activity type) when

- a task is completed (could be set ‘regarding’ any table)
- a survey response is received (also could be set ‘regarding’ any table)
- a marketing form is submitted (could be related to a lead or a contact)

# Filtering on Lookups in Triggers, Journey Branches and Email Content in Dynamics 365 Customer Insights - Journeys

How to filter in Journey triggers, branches and email content with Lookup column values, rather than filtering on the name of the lookup and feverishly hoping someone doesn’t change the name, or that you spell it wrong.

# Lead and Contact form Insights tab in Customer Insights - Journeys (without editing Form XML)

The Insights tab for Leads & Contacts in Customer Insights - Journeys shows marketing interaction data (email opens/clicks, form visits/fills etc.) for both real time and outbound marketing on the Contact or Lead form. You can now add this to custom forms using a drag and drop form component in the Power Apps maker studio form designer. Yay!

# List, Filter and Delete Flows in Power Automate

A simple little flow that can be used to list and filter flows, to do whatever you wish, and in the example of the dreaded *CXP_* gremlin spawning I need to delete them.

**Why would you need to delete so many flows?**

When you create a Customer Insights - Journeys ‘Journey’ it creates multiple power automate flows in the background with the prefix *CXP_*. Each journey can have 5+ flows running behind the scenes, each time you edit the journey it creates even more. Once the journey is complete or stopped, the flows are automatically turned off and left to fester in the default solution forevermore. Deleting these flows does not result in any loss of analytics or data. Once their job of automation is complete, they are obsolete.