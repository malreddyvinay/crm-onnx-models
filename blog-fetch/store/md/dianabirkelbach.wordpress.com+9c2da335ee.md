All PCF learning resources: from prerequires, pre-required knowledge, development, debugging, ALM and more advanced topics like theming, Fluent Ui 9, events or drag6drop. Content from Microsoft Learn, my blogs and other community resources.

# Inside Built-In and Custom Copilot UI Widgets powered by Power Apps

Custom app-powered Widgets feels like one of those shifts that will change how we think about Copilot experiences. Until recently, a lot of the conversation around tools was still very text centric. I love nice colorful surfaces, letting the eye catch the main points in one second, without having to read a lot of text.... Continue Reading →

# How to make Deep Links with Code Apps and call them from Model Driven Apps

One of my Code Apps is going into production, and I thought it is a good time to finally take the time and start blogging about Code Apps too. Just in case you are not familiar with Code Apps, it’s about creation of complete Apps using Code (React), and hosting it inside Power Apps, while... Continue Reading →

# Navigating to and from Generative Pages

Generative Pages are a great way to create custom UI in Model-Driven Apps. But of course, the pages are a part of an app, not standalone, so we need to know how to integrate them into the model driven app. This blog is just a beginning. There are missing features. But since we have some... Continue Reading →

# My TimeTracking Page using Generative Pages and Fluent UI 9

My purpose for this blog was to take a Custom Page for Time Tracking and re-implement it using Generative Pages. But the page should look like the rest of my Model-Driven App, so I wanted to implement it using Fluent UI 9. I'll use only GTP-5.0, since it's already available. The custom page was just... Continue Reading →

# First Look at Generative Pages in Power Apps

With Generative Pages (find announcement and docs here) we can create a page in Model-Driven Apps using natural language. You can see it as a reimagined Custom Page with two differences: You don't need PowerFx to create it. You just need to explain what you want. The result is React code, which you can see... Continue Reading →

# PCF🩷Copilot Studio: First Look at Agent APIs

You probably saw already the exciting Copilot Studio possibilities coming to Model-Driven Apps. If not, here is the preview announcement. Basically there are 3 ways to interact with Copilot Studio from Model-Driven Apps: Agent Xrm API (Xrm.Copilot) : a set of functions under the Xrm namespace, allowing us to call Copilot Studio topics using MDA... Continue Reading →

# The magic of pfx-default-value for PCF – with example on how to provide colors

We know since the beginning that the PCF properties have a "default-value" which allows us to define a default configuration value for the properties in model-driven apps. It is documented that this is allowed only on input properties, since the bound parameters expect to have a column associated. I think they are interesting only on... Continue Reading →

# How to Detect that a PCF is Running Inside a Canvas App / Custom Page

Usually my target is to develop a PCF working inside all types of apps: Canvas App (or Custom Pages), Model-Driven Apps and hopefully also inside Power Pages. But at least between Canvas Apps and Model-Driven Apps there are slightly differences (or huge 😉 on how to handle the code, and I need to add some... Continue Reading →

# Debug PCFs using a Browser Autoresponder Extension (MDA & Canvas Apps)

I'm sure the Autoresponder idea for Debugging PCFs (or WebResources) is not new to you. Debugging with an autoresponder solution is a life saver, since allows you to see the changed code without having to upload it again: you just redirect the file/webresource to a local file (the bundle you generate locally), instead of loading... Continue Reading →

# Two Way Communication with the Form Component Control

The Form Component Control (FCC) is not new, but still awesome! I have an older blog where I wrote about the FCC and the meaning for PCFs. Lately I had a special request about a subgrid, and my answer was FCC. But I had to figure out first, how to let the form communicate with... Continue Reading →