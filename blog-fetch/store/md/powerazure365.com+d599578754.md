# Automation ALM Power Platform / Dynamics 365 CRM

# **Introduction**

## 🚀 Automation ALM for Power Platform and Dynamics 365 CE/CRM (Dataverse solutions)

**A solution to improve the ALM process in Power Platform and Dynamics 365 (CRM/CE). This solution is based on top of the ALM Accelerator made in the CoE Starter Kit.**

This new article I just made in August 2024 is here to explain how to do better ALM process for Power Platform in general. This topic is also important to consider even if you are coming from D365 F&O space like me. I will pick 1 basic example (among many others) with the convergence and the fact that LCS will be shut down in the coming months, and we will come up into PPAC (Power Platform Admin Center)

As you know, when you are now wants to deploy Electronic Reports (ER) in the new Globalization Studio, you have a Dataverse behind to store any change in a solution. You should be able to deploy easily right ? You should store into Azure DevOps and release it from Dev => Test => Prod

You have made Power Apps, Power Automate, Virtual table stuff (on Dataverse linked to your F&O instance) and again you want to use Azure DevOps CI/CD like you already do for F&O (X++) part.

So this new solution I just made, on top of ALM Accelerator that is quite well known in the area of D365 CRM space, is likely to be for anyone in Power Platform / D365 space (even Business Central 😊 - and F&O folks like explained just before)

What I will check in the coming weeks is : How can we now Unified the ALM process between F&O and Power Platform together with the Unified ALM Experience already available. We will not deploy the code anymore through LCS, but on PPAC with UDP (Unified Deployable Package) . I already talked about it here in my blog. So, how can we deliver in the same package components that are only in Power Platform (Power Apps, Automate etc…) with also the X++ compiled into the same Dataverse, deploying also in the right order (F&O first, then PP only ?) - I opended this discussion here. And surely my point will be to check how can this be done through ALM Accelerator and this new solution I have made.

But enough F&O for the moment 😙 - Just below is my Github Repository. I will suggest to read it, you can download the solution, have a discussion space, issues space, and start also the journey with me to enhance it for everyone.

So before jumping to this topic, why I have done it ?

My goal is to give to the community a solution for Power Platform to improve ALM process in terms of deployment. While the ALM Accelerator for me is the best tool (coupled with an Azure DevOps to manage solution deployment), it was still a manual process to release Dataverse solution. Coming from a D365 Finance Operations background at first, it was for me important (as a lazy guy) to decrease the amount of time needed to release something on a Dataverse environment !

Here's why:

- Your time should be focused on creating something amazing. A project that solves a problem and helps others
- You shouldn't be doing the same tasks over and over 🔁
- You should have a quality/rigorous release package for each new deployment without manual actions 💆♂️
- No manual deployment for Dataverse !
- Your source code is on GIT Control
- No direct code WITHOUT a solution ! No direct code in Production, no code in the Default environment (yes believe me I have seen those things 😒)
- Pipelines from Microsoft in managed environment are not good (at this point of time I write this article - with a lot of limitations)
- The solution will help you to manage the process in which sometimes Microsoft will also release something on your Dataverse at the same time as you. (Retry process)
- You want to pre-schedule a release BEFORE and not waking up at 03.00 am to launch it in Prod…

My solution is *just* on top of the ALM Accelerator solution. I will cover just below after how to first install it and configure it ; before talking about my solution I have made.

The ALM Accelerator is a very good starter kit to configure a DevOps for Power Platform (end to end) and avoid taking a lot of times to configure it on your side manually. With the Automation ALM in top of it, believe me, you will save a LOT of times !

# **Azure Dev Ops**

You should have created your Azure Dev Ops organization on your tenant. If you have already created, you can skip this step and go directly to the configuration part only.

Remember DevOps organization is free, you have 5 basic users for free and also including 1800 minutes of build per month. You can after link your Organization to an Azure subscription if you want more.

For all those steps, you will need an account with enough permissions in the tenant (for now on to create DevOps Orga and even after for ALM Accelerator) :

- A licensed Azure user with permissions to create and view Microsoft Entra groups, create app registrations, and grant admin consent to app registrations in Microsoft Entra ID

- A licensed Azure DevOps user with permissions to create and manage pipelines, service connections, repos, and extensions
- A licensed Power Platform user with permissions to create application users and grant them administrative permissions

So to create a DevOps organization for the first time, you should go to : dev.azure.com / Start free

**After you don’t really need to create the project yet**, since we will create it through the ALM Accelerator Model Driven App

Go directly to the Organization settings, **now this part is for everyone !**

Again you can setup billing like this, as you can see we have the 1800 minutes for free. BUT, there is a but, you still need to ask Microsoft as a private project to fill this FORM (just 1 time) - see more details here too.

Now we will review and change or not some settings you have by default in the Organization settings

- Third Party App via OAuth
- Allow Guest Access if you like also in the Policy
- Authorize still classic build pipeline / release pipeline just in case ( **especially for F&O people** ). Even it will be via YAML files for ALM Accelerator
- Last one ( **for F&O people only** ) you can go to the repository settings and activate the TFVC (by default, it’s blocked) :**Disable creation of TFVC repositories -** Disable creation of TFVC repositories. You can still see and work on TFVC repositories created before.

Last step for DevOps is to activate some extensions that will be needed for ALM Accelerator.

- **Power Platform Build Tools (required)** : This extension contains the Microsoft build tasks for Power Platform. (https://marketplace.visualstudio.com/items?itemName=microsoft-IsvExpTools.PowerPlatform-BuildTools)

- **Replace Tokens (required)** : The pipelines use this extension to replace tokens in configuration files and store secure values in private variables configured for a pipeline. (https://marketplace.visualstudio.com/items?itemName=qetza.replacetokens | https://github.com/qetza/vsts-replacetokens-task)
- **SARIF SAST Scans Tab (optional)** : Use this extension to visualize the SARIF files the solution checker generates during a build. (SARIF SAST Scans Tab - Visual Studio Marketplace)

On Azure now, you should create an Azure App Registration, for this I will suggest to check this part on the MS Learn directly.

# **ALM Accelerator**

Now we are good to go, we can install ALM Accelerator. I would suggest creating a specific “technical” dataverse, in which you can also install if you like the CoE Starter Kit. (Remember that ALM Accelerator is also standalone, so you don't need to have both together) . If you don’t have enough Dataverse capacity (that’s usual 😁) , you could also install it into your DEV environment. Install those managed solutions into it, in this order :

1. Creator Kit latest release - Download it here
2. ALM Accelerator latest release *March 2024* - Download it here

During installation of ALM Accelerator, you will be asked to setup Connections, for the HTTP with Azure AD you’ll have an error like this

Just put the Graph URL : https://graph.microsoft.com/

So then, still the “Import” button will be grayed out. Don’t be afraid, Microsoft bug ;) , just go back and relaunch the next

Wait 5/10 minutes, and you’ll have everything installed like this :

Post installation, you just need to setup the DevOps Custom Connector used by ALM Accelerator. On Maker Portal of Power Apps, click on the “… More” / Discover All and find the Custom Connector part, that you can pin now.

Then you can click on the Edit button.

Click on the Security tab and Edit button.

Then, you need to enter all the Azure App Registration you had created before. **Authentication Type : OAuth 2.0**

**Identity provider : Microsoft Entra ID**

**Client ID :** The **Application (client) ID** you copied when you created the app registration

**Client secret :** The **Application (client) secret value** you copied when you created the app registration

**Tenant ID :** Leave the default value, **common**

**Resource URL :** The **DevOps Application (client) ID** you copied when you added permissions to your app registration

**Then Click on Update Connector.**

Confirm that the **Redirect URL** on the **Security** page is : `https://global.consent.azure-apim.net/redirect`.

If it isn't, copy the URL. Return to the app registration you created earlier and replace the redirect URI there with the copied URL.

Try the connector just to be sure like me, you should have something like me (after creating also your connection) , try a GetOrganizations , return 200 (OK)

Now we are good, we can run the Model Driven App to setup the project of DevOps, initialize the git repository, pipelines, branches etc…

By Going to the Project part, we will initialize everything.

Use the included wizard to set up your Azure DevOps project to deploy Power Platform solutions using the ALM Accelerator. You can configure an existing empty project or create one.

1. Open the ALM Accelerator administration app.
2. In the left side panel, select **Projects** in the**Azure DevOps** group.
3. If you're prompted to update **Release Tags** , select**Okay** .
4. Select your Azure DevOps organization in the list.
5. In the **Projects List** , select**New** .
6. Select **Project Wizard** .
7. In the **Project** step, enter the name of your project. Optionally, enter a description and enable preview features.
8. Select **Next** .
9. In the **Pipeline Templates** step, select**Next** to install templates in your project.The app installs the pipeline templates into a new repository in the project. Alternatively, you can configure the project to use templates from a project that already has them installed.
10. In the **Service Connections** steps, select the environments for which you want to create a service connection.**(DEV, VALIDATION, TEST, PROD : All your environments in which you would like to use ALM Accelerator)**You can select multiple environments and create service connections for all of them at the same time. To use different app registrations for your environments, create a service connection for each app registration individually.
11. After you configure a service connection for an app registration, select **Add** .
12. After you've configured all the service connections, select **Next** .
13. In the **Generic Pipelines** step, select**Next** to create the pipelines and variable group and set the Azure DevOps permissions the project needs for ALM Accelerator functionality.

You need to add the App Registration for each environment you have setup before in PPAC (as System Admin) / S2S Apps. Like this :

**Set up makers to use the ALM Accelerator app**

- Configure user permissions for a maker's account in Dataverse and Azure DevOps.
- Configure deployment user settings to set up the app's user experience and grant access to solutions and deployment profiles.

My side I have created mine like this (Allow everything - because I am the IT Admin) but you could change for each people differently. *For my Automation ALM after, I will suggest using a dedicated service account, that have those kind of permissions.*

After a change on DevOps side in April 2024, don’t forgot now, to review this TOPIC ! Otherwise some pipelines will not trigger (like validation policy)


Double check that the ALM Accelerator account can create policy for the validation build pipeline

We have finished with the model driven app for now, so you can close it. **Of course, remember, that everytime you have a new environment (especially DEV environment) you should create the service connection through this MDA in the DevOps part, and add also the App Registration on it.**

Now we will discover the Canvas App that everyone can use, and those steps are not replace by my Automation ALM Solution, so important to know how it works : because those kind of steps should still be done manually. Well, be aware, you will not change that every day….

Select the right Maker environment (the DEV environment) in which you have unmanaged solution to deploy and commit through ALM Accelerator

Select one solution and create your first profile ; and still to be done in the future if you need a specific one because I want to deploy this solution in others targets environments.

Select the right DevOps Orga + Project we have setup before, the Repository too (normally the same as your project name) and also Use the Solution Branches naming convention. Select for each, your validation + test + prod environments. Remember you have it in the dropdown list only if you have created again before in the MDA as Service connections.

After saving, the solution shouldn’t be grayed out anymore. So you can repeat that for others solutions if you like. This step should be done also after creating a new solution (like in 1 month I didn’t have it before, first time to setup it in ALM Accelerator). **You will need to do it before using it with my Automation ALM Solution. Again you do it just 1 time ! Or if you like to change the destination environments too.**

So now, we will do a VERY important step and that’s also the very good thing about ALM Accelerator is : setup settings deployment solution. After all, when I do a new deployment I want maybe to activate this flow, not this one, put the right owner, put the same service connection for all of them, put the good environment variables, shared my canvas to this group of users etc… : well you have a lot of things !

Good part here is : I use in fact my side ALM Accelerator for the solution I just released in my GitHub for you, so good example ;)

So click on “Configure Deployment Settings”. Good reminder, this step needs to be done 1 time EVEN if you don’t have anything to change about settings ; **and again this step is mandatory for my Automation ALM too. Again I don’t change ALM Accelerator, I am just releasing something on top of them, so process is the same as if you were using it manually end-to-end.**

Repeat those steps after for each environment (Validation + Test + Prod)

For each tab, please review it. **For the Connection references, please don’t forget to click on Share tickbox everytime.**

For Flows, I would suggest to change the owner also, and put a dedicated service account that have of course Power Automate license. My side finally, I often use upgrade solution just to be sure to clean up everything correctly if I delete something. This will increase the time of import in Dataverse, but more safer.

**Of course each Maker or ProDev should inform people when they create new stuff ! (Like Flow, or environment variables) in order to update it too.**

So now, I can show quickly how it works if you want normally to NOT use my solution after, but still use the standard process of ALM Accelerator.

After all, it’s good to know because **you can see what I “replace”**

So here before, I can click “Commit Solution” when I am ready to go in my DEV and finish my requirements / work items. (*By the way since you have deployed an Azure DevOps now, you can also use it for your backlog, sprint etc…)*

This will create an export solution GIT pipeline behind the scene, publish all customizations, and export both as unmanaged + managed solution. The source code behind each components will be synced too. It’s as you can see a “TEMP” dev branch. You select the target branch, which the Solution Branch Name (like me here “test1” is the name of my solution). You need to wait of course that the pipeline is finished.

Then, when you are ready to go the next stages, you click Deploy button

You need to select the Source Branch => Target Branch 

- So if you select the DEV branch we have created before during the commit solution as the SOURCE and then the Solution Branch Name as the TARGET it will trigger the deploy-validation-pipeline and also create a Pull Request of it. So you can say, please automate the closing of my PR or not. This will then merge it to the Solution Branch Name that will also trigger after the deploy-test-pipeline.
- For Prod, it’s kind of same thing, just you need to select the Solution Branch Name as SOURCE and “main” as TARGET. Again a PR will merge the code and launch afterwards the deploy-prod-pipeline

And that’s it, you know very well ALM Accelerator now :)

We can go to my extension now on. So globally, my goal was to replace the process of the COMMIT and DEPLOY solution, but I imagine you can compare it with or without my solution and see hopefully how it can also help you to be more agile and avoid doing those 2 steps manually.

# **Automation ALM**

## 🚀 Download the latest release

To get the managed solution to install, download the ZIP on the latest one available HERE *Latest Release March 2025 - v1.0.20250327.1*

## ❗Prerequisites

As explained before, my solution is on top of ALM Accelerator, as a reminder you should install first those 2 solutions. If you need help on how to install and configure it, you can read again the part of it in my article here.

- Creator Kit
- ALM Accelerator

I am using 3 types of connectors (just make sure about any DLP policies you have in your tenant of Power Platform) - Azure DevOps + Dataverse + Outlook Office365

## 📖 Installation (first time)

*Below is the intrusctions to use the solution.*

1. Install it (the Dataverse managed solution)
2. For the Connection references, use a service account and dedicated one that have access to the DevOps Organization and Project with the right permissions. Same thing for the Dataverse connector. You could setup a different one if you like for the Office 365 Outlook
3. You have multiple environment variables to setup too. A dedicated Flow (after installation called : *0 - Setup - GetDevOps Config* will help you to fill 3 of them : ApproverId + RepositoryId + ExportGit) so at first you could leave it empty for those 3 ones.
4. Go to the Model Driven App installed, **change your personal settings with the right timezone** . You could also share it to other users in your Dataverse.
5. Change the default view on the Environment variables section in the Model Driven App, my side I have added the field *Environment variable definition* + doing a filter on (start with)*dyna_* and then after pin as the default view and share to everyone.**You could after review the list and check if all is good.**
6. Then, Activate FLOWS and in the right order ! Yes, there are 18 Power Automate. I made it normally simple based on the name and the number convention (to read it like an order by DESC 😄) so 99 first and last are 10

On the Model Driven App, in Settings Group, you have to create your DEV environment(s) (with a / at the end) , the URL should be the same as the service connection name in DevOps you have setup in the ALM Accelerator before. Create also all your solutions you have activated with ALM Accelerator Profile. Finally, you could also create your Power Pages (name could be retrieve in the Portal Management Model Driven App) *Be careful this part is only for Power Pages in standard model and not the enhanced model* - For enhanced model you could just put your Power Pages site on a normal Dataverse solution for ALM Process

You are now good to go for the Usage part 😈

## 📖 Upgrade to the latest release (when I will release new one each month - See again my GitHub Repo)

Just install it as an upgrade process in your Dataverse. Double check that each Power Automate flows are still "ON" after. I will in each release specifiy if there are any manual post actions or any new flow to activate.

## 📚 Usage

First, you could also check my LIVE Demo in YouTube here.

So in general, remember here that you need first for the solution you want to deploy automatically to assign an ALM Profile in the ALM Accelerator Canvas App. Also, you still need to setup the *Configure Deployment settings* for each step (Validation,Test,Prod) in each solution. Globally, I don't replace those 2 parts, you still need to do it BEFORE using it with the AutomationALM.

But then, you can create ALM Deployments. I support 2 types as of now : : Validation then Test, Production

I will add somehow multiple other ones in the next release : like From Dev to Prod directly (end to end), **or also having multiple DEV environments when multiple makers work on the same solution** and wants an auto merge+PR before deploying, and finally to ReSync automatically (like a Get Latest version as unmanaged) their DEV environments right after.

Assign your DEV environment in which your solution(s) are installed in unmanaged, and of course the right ALM Profile explained before.

You have 3 types : right away, on-demand (delay until a datetime), scheduling.

**For the scheduling you need to have a format scheduler in ISO 8601 (e.g I want to deliver this solution each day is PT1D, each week : PT1W , every 12 hours : PT12H) : exactly the same as the timeout of Do-Until in Power Automate**

Click Save, then assign all the ALM Solutions in the right order you want to deliver. I support the same Commit Scope we have seen in the ALM Accelerator part before : Solutions and Settings, Solution Only, Settings only, Power Pages only (so very useful if you just want to push an environment variable value without the complete solution)

Here of course by default, it’s in Draft reason status. So nothing will be done until you do something which is to click on “Launch button” on top !

Before doing that, I want to highlight something which is quite different here from the ALM Accelerator Canvas App. 

Yes, you can NOW pre-schedule anything in advance !! I mean like I want to push those 3 solutions into Prod at 4.00 AM without waking up…

Could be something with a recurrence or not.

That's it 😄

So when you just click on “Launch it” button - the status will go from Draft to “In progress” or “Waiting” depends on the Type - it’s here where the magic happen and you can do whatever you like to do instead waiting that each step has been finished before doing the next release manually. At the end it will be in “Ended” - if it’s right away, you can just click “ReLaunch it” at any time to launch again the same thing over and over. Or you can also clone it if you just want to change something (Like a Release 1 with those 3 solutions and another deployment Release 2 with just 1 solution only)

You will have of course an history log attached for each steps. Speaking of which, something quite interesting here, is the very big flow I have made called “Check Progress” : this one is dynamic and check if we can continue to deliver the other solutions or not. Also this flow sent an email in case of an error on your side (like missing dependency) , but if it’s Microsoft issues because they push a LOTTTTT of solutions each day in your Dataverse and you don’t want to wait and relaunch it manually…. That’s why I have put those 2 environment variables called : RetryMaxMinutes (12 by default) + NumberOfRetry (5 by default)

At the end you can also clone an existing deployment, or even ReLaunch it if it was of type "Right away"

You can also access in this case the Model Driven App via a Mobile (Power Apps iOS / Android) to remotely launch an existing deployment you already have done before, or pre-existing one.

Finally, I do also some “cleanup” stuff when nothing have been changed (between the export 1 and 2 for example) from your DEV to other stages. Right now in ALM Accelerator, you have a lot of “TEMP” Dev Branches, and also a lot of export git pipeline in partially succeeded. I still keep it in the history with status “NoChange” for you ; so that you know especially during a recurrence deployment each day or each week that “Ok deployment done, but well nothing have changed since last time” , useful especially you don’t know everything developers do each day and maybe they don’t remember on which solutions they have made something new or not since last time.

## 💡Roadmap / Subscribe

See the Project Roadmap for the backlog and current progress.

See the open issues for a full list of proposed features (and known issues).

Don't forget that you can subscribe and get notifications on the repository for each new release, issues, discussions etc...

## 👐 Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please open an issue with the tag "enhancement". I have shared now the source code, if you want to contribute with me, go the Discussion space

Please fork it, create your branch and a Pull Request

Don't forget to give the project a star! Thanks again!

## 📝 License

Distributed under the MIT License. See LICENSE in the repo for more information.

## 📢 Contact

Aurelien CLERE - @aurelien_clere LinkedIn : Follow Me

## 👐 Support me

While I always do everything for free for the community, if you want to support me you can do it here

## 👐 Acknowledgments

## 📚 Other Resources

# **Conclusion + Demo**

Hope you will like it. As explained just before, I will be happy if you can try it yourself and give some feedbacks and enhancement ! Please check the GitHub Repo again for that. Thanks.

Now, of course, the last part that neither ALM Accelerator or my solution cover (yet) is : How I make sure that when I will do my Prod Rollout, I will pick ONLY Dev that have been validated (like picking) some commits, and not those ones. For that, you can still do it manually via GIT in DevOps if the process have been done correctly via work items assignments. So we have still work to do to be perfect. Could be also a small solution done for each new requirements and merging in the superior branch to the one global solution. Like for a lot things in life, ALM is also with a lot of debates and how is the best way to deliver code correctly. Mine is 1 option, maybe not the best one, but I think enough for what I have seen so far during projects.

Here is a video to show it in LIVE for you

Enjoy !