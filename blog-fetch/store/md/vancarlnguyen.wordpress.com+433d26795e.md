Are you one of many, including myself, that performs CRUD operations using JS (when it fits, for example when you have certain dependencies to a form event)? Well, you should think again about where you want to perform CRUD operations!

**Introduction**

Most of you probably have searched 🧑💻 something like “JavaScript vs Plugin”, to understand when to use js, plugins, workflow, etc. And you will stumble upon great answers by many people in the community! Examples of very common cases:

- When you need to perform UI changes in real-time. For example, locking fields/sections based on a field value or form state.
- Trigger logic before any server-side logic/validation.
  - Such as OnLoad, OnChange & OnSave

**TLDR**

- Move your CRUD operations to server-side code (C#):
  - Custom Workflow
  - Custom Action
  - Low Code Plugin: Instant Plugins
- JavaScript introduces issues on the client-side
- C# Approach:
  - Saves time in the long run
  - Helps your junior to understand the process/business requirement more with unit/integration tests.
  - Provides more quality code.

**Problem**

**Problem 1:**

As you may know, JavaScript runs on the *client-side* rather than *server-side.* This means that the code runs in the context of the user’s browser and not  the server. What does this mean? It means that each user’s browser setup/config is unique, which leads to different experiences when using the system. 

For example a common issue that my colleagues have is that after I have published my JS changes, the new code is **not always** loaded in their browser after a refresh. So they perform hard refresh again, again… and again. And finally the new code is available. Even clearing the cache is not always the solution for some reason.

Another example is that they don’t have the same browser version as you! Or may not even use the same browser! When Microsoft introduced their new “Look” to D365 CE, if you didn’t have the “correct/latest” version then you’ll experience some issues. Like, the text message in the dialog box that was missing (speaking from experience).

**Problem 2**:

This is my favourite part and main purpose of the blog post, you can not do quick automation tests! And before you cross ⚔️ your arms and say, yeah but we have Selenium 😎. But it is not fast, and it depends on many factors to make it work 😩.

**What else to do?**

Move your JS CRUD operations to Custom Actions, Custom Workflows or even perhaps Instant Plugins! Why? Because it can be easily tested! Although for Instant Plugins, you can only do integration tests, not unit tests.

**Development & Testing Process**

Consider the example below, a process where we want to create a new opportunity with a reference to a project which has 5 related tasks. The process is executed from a ribbon button on the account record.

Imagine the process of testing this process in JavaScript 😩 Let’s take a look at the javascript diagram on the left side below, it should describe the pain and misery in your head. You might be thinking, yeah but it only differs one extra step 🤔?… No, not just one extra step (refresh browser). Many more steps (in total) if you count number of times you must repeat the process until you meet the business requirement.

Let me walk you through the process of each approach.

**JavaScript:**

1. You start developing your code in vscode or notepad
  - You add some validation logic and error handling here and there
2. You deploy it through XrmToolBox or directly in CRM.
3. Refresh the page that shall load the new code.
  - Sometimes, the new code is not loaded. The old code is still cached and active.
4. You trigger the code, but noticed the new code hasn’t been loaded into CRM. Go to back to step 3, and repeat until it runs the new code.
5. The new code is finally loaded, as you see in the breakpoint (if you’ve set one).
6. An exception occurred due to whatever reason, go back to step 1 and start over.

The steps 3-6 are, in my opinion, the worst part. As you need to manually start the process from scratch. I’m sure that you’ve encountered a scenario where you need to re-enter certain values to fields on the form before triggering your javascript.

**C# – Custom Action/Workflow:**

1. Create your plugin code
2. Write your tests, unit and integration.
  - Go back to step 1 if the criteria isn’t met.
3. Deploy the code using plugin registration tool & webresources manager (XrmToolBox)
4. Test it in CRM and repeat from step 1 if needed.

Developing the example process using JavaScript might have a quicker implementation time, depending on the business requirement, but is prone to more errors (human & technical error). While C# may take more time it comes with more quality ✅ and reduces time ⏱️ for future change requests and troubleshooting. Your junior will thank you for the tests you’ve written, and definitely the customer as well… at least indirectly.

Hold on a second! You still need to write javascript even though if you’re going with C# approach. Of course, but most of the logic will probably be placed on custom action/workflow. You just need to write a javascript that calls it!

As you can see, you may require more code for the C# approach but you can write tests and test it quickly!

It’s not all pros with C# approach. One of you might be thinking yeah but… now you have code in JS and C#. It is too messy 😩. Yes! That is a very valid point and could possibly be a decision maker as well. Having code spread all over different areas introduces additional administration 👷. But for this case, it also means that you are able to disable/enable the custom action. See it as a feature toggling. That does not come with only developing JavaScript.

But what about the functional consultants? They probably won’t even touch plugins and such, but they are more prone to play with javascript. Because it require less tools to implement code logic and perhaps feels less scary 👻. Well, to be honest I don’t blame them. It is less scary because you can do “more damage” with plugins. For example, if you implement a javascript on a form, it’ll be applicable to only that form. But if you were to add a plugin (talking about normal plugins) it’ll trigger on the table level.

And now you’re probably thinking, yeah but you’re developing on the dev instance so it should be fine. Hah! 😈 No, not all projects are super strict with implementing hotfixes 🛠️ through solution deployments/pipelines and that is fine, **as long you know what are doing and that you know how to revert/remove it before the big deploy.**

**Final words**

If you know your CE project will have a lot of custom code and that it’ll probably change with time, and different developers will be involved then C# approach is something to consider.

In my opinion, don’t perform CRUD operations in JS unless it’s something very basic/simple! You will save troubleshooting time and headache, and also the time you assist your junior.

Another thing, this will be a great addition to your automated tests in Azure DevOps! See my post about D365 CE tests here Part 1: Setting up the pipeline and Part 2: Involve your team!

## One response to “Power Platform – D365 CE JavaScript: CRUD:ing somewhere else!”

While I agree with your approach, you should also consider using Fiddler to simplify your JavaScript testing process.

LikeLike