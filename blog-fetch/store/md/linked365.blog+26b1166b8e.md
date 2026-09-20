In my role, the ability to curate and control source code is essential. In the Enterprise Development space, the desire to put complicated, costly solutions in place to monitor the application and ensure that only quality, bug-free solutions are deployed is high. But, there is more than one way to ensure quality, there is more than one standard for quality, impacted by the requirement for each solution and your organisationâs approach to data and risk.

In this post, I wanted to highlight what I see as the 6 (+ none) variations of code deployment, focus on how they apply to the Power Platform, and provide an insight into why your organisation should choose this way.

Bear in mind, as has been said, the choice you make depends on your organisation, your maturity, your desire to control the amount of testing required, and your partner’s tools and abilities. What this does is give you much choice and a lot to consider.

This is also solution-dependent. Do you want a full-blown, fully automated test coverage for a SharePoint app that your account administrator (ð to Linda) made to simplify the invoice management process? Do you want no testing for your mission-critical, complicated solution across multiple domains or deep integrations between composable applications?

## Things to Consider

When you are deciding on what method works for your app, there are 4 options to consider. With any application, the levels of each can shift as the application matures. For example, a feature is added that effectively moves the needle on criticality to high, as it now is part of the core function; the complexity reduces as you have managed to bring the legacy application that needed APIs and service bus to integrate with into the main app.

### Criticality

Define what the impact on your business would be if the application didnât work. What is the data in the system worth to you if it is deleted or is shared? Less critical apps (for most businesses), such as Desk booking, recognition apps and simple improvements to email automation, do not have the same impact on your business on failure. Yes, it may be painful for a few, and harder work for a while, but your business will still operate.

Consider your ERP system or your ability to stream video (for the Netflix/Amazon Primeâs of this world), if these go down, so does your business, making a financial loss for each minute that it is not available.

What about your CRM or HR system? Probably not critical to run your business (you can still discuss opportunities, create service tickets, sell coffee or whatever you do, but the data it holds is very sensitive. Any data breach because of an app update could be business breaking, from a reputation point of view or a legal one, with GPDR and other considerations meaning your obligations to ensure the security of this data is critical to your organisation.

### Complexity

Define how complex your solution is. If there are a lot of moving parts that have to be aligned to ensure the application performs in the appropriate way, then it is essential to ensure your testing regime for all the constituent components is adequate enough to prevent data and functional issues.

If you have a front-end portal, service broker and back-end database, aligning the functionality, data map and requirements for each is essential. Ensuring each knows about the additional field, what data type and how to use it when you deploy one of the parts will be necessary.

These complex solutions tend to require full integration testing and full regression testing to ensure what has been added will not break any other functionality.

### Cost

Full testing every time you deploy an application is not only time-consuming, it can cost actual money. This is not only in the cost of the licensing or software but the infrastructure to run the operations.

In the Power Platform, you have only so much capacity; this will have to be managed to prevent sprawling applications or increase the capacity you have available at an increased cost.

There is also the time constraints. As your regression testing library grows, the time taken to deliver a project into an upstream environment can be detrimental to the SDLC you have deployed. When the testing is taking longer than the dev effort, you need to reconsider your strategy.

### Capability

For Linda from accounts (a character that Mr Huntingford and I use to denote an IT literate, empowered app maker), solutions, environment strategy and ALM are not even words in her vocabulary. All Linda wants is to have the app she has made available to her colleagues in accounting.

As your app complexity increases, the requirement for someone to configure and maintain deployment pipelines will increase, utilising the out-of-the-box Power Platform pipelines to full use of GitHub actions or Azure DevOps.

Maintaining these processes in and of themselves can be a full-time role, particularly as more and more parts are added to the solution.

## Some Options to consider

### 0 - No Source Control, no Deployments

Developing in production is normal; SharePoint, as an example, where you are editing lists, defining forms and doing so in the same environment as your users will be creating and editing data. Not to say there are mechanisms to put in ALM for SharePoint, but your usual developer will be updating and creating solutions in one environment.

This will also apply to some Power Apps, anything you create in the default environment. You do have version control at this stage, being able to roll back versions of an app, but you are very limited.

This state is only for personal productivity apps. Those that are very low on the complexity level, do not have any impact on your business (apart from an upset Linda ð), come for free in terms of any additional cost and can be done by any app maker in your business

### 1 - Dev/Prod with rudimentary, manual deployments

This is the first option where there is some thought: you have a dev environment separate from your app’s users. But simple deployments, copy/paste of list settings, duplication of configuration between two systems and, at the most, export of an app or one of its components and import into the higher environment. Your source control is the development environment, along with any files you have saved to move the apps to production.

This will typically be where a citizen developer, directed by some control from your IT administrators starts. Apps that start and continue to be developed in the Personal Productivity environment are usually here.

Again, this is not for critical apps. Donât allow this simple process to happen for anything more than personal productivity, as the risk is too high with no control. Every app maker should be able to get behind this simple process, though, and there is minimal (Everyone can have a developer environment) cost to your organisation.

### 2 - Dev/Test/Prod with solutions

Defining solutions, backed as you must with Dataverse, is probably the minimum you need to be doing for an app with more than a low criticality. Your solution control is still in versions of the solution you have saved in a file system, but you have a rollback via these.

You also have the ability to create managed versions, controlling the changes that can be made in higher environments. This allows you to roll back with ease when something goes wrong.

Your solutions are still moved and imported manually, and who ever is moving these solutions needs access to production, but business process in your organisation will decide when enough testing is done.

DevOps, as a means of controlling the list of works, tends to start at this point. The use of a board to control the progress of stories and issues gives more visibility to the whole team, pushing away from the nightmare spreadsheet I remember in my early days.

Most organisations will be utilising this as a standard when external or dedicated development projects exist. You will need the coordination and control managed solutions brings, at least knowing that you can revert back to the last know good state.

With the introduction of solutions, a level of understanding and control needs to be added to your simple development process, which will minimally impact the complexity, cost and capability required.

### 3 - ALM with Solutions

As you get more complicated, this is where automation starts. Still working with solutions and the out-of-the-box tooling, you can put simple approval processes in place to control when solutions are moved to your other environments. This should be a business user or tester that has this approval.

Utilising Managed Environments functionality, a simple DevOps pipeline can be created. It takes effort and administration, but it can also segment access to higher environments. The user that is running the deployment process and pushing the code to production does not have to be the developer.

Managed Environments do allow you to trigger a Flow and work with more complex approvals and source code integrations, but not the complexity or control as shown in the next stage. These simplified pipelines also allow for prevalidation steps, including checks for dependencies, and environment variables. Versions of your applications are also stored as managed and unmanaged versions within the pipeline host environment.

For most apps considered important to your organisations and need to separate access between development and production, this should be the starting point. The control presented, even though limited, allows approval automation, putting decisions to deploy away from a developer. Utilising Managed environments in itself does mean you need a license, but if you are using Dataverse in your solutions, this is part of the package. Somone does need to configure the pipeline, but as it is part of the application, it is a few clicks and decisions.

### 4 - Use of External Tooling

Azure DevOps, GitHub actions or any other ALM tooling provides a level of control that you don’t get in out-of-the-box tools. There are plenty of tutorials available on how you can create your own process.

This allows a lot more flexibility to your ALM process and is the gateway to test automation. Azure DevOps and GitHub actions allow for periodic or multiple builds, which isnât possible with the managed environment configurations.

At this stage, you should not be utilising the solutions defined by your developers. This is where source control comes to the fore. Checking in the code, merging the components and then defining downstream builds from source control rather than solutions allows a granularity not achievable previously.

Configuring these pipelines is time-consuming and needs a level of understanding different from Power Apps. People make great careers by specialising in DevOps. This, along with Azure DevOps or other tooling costs will add to your budget but brings more control and confidence in the build process.

### 5 - Full ALM with a suite of Tests

Automatic testing is fundamental for most enterprise organisations, as it allows confidence that any improvements donât break what has come before.

Utilising regression test suites in your UAT environment or in an SIT (System Integration Testing) environment prior to UAT will reduce the risk of issues being found later down the chain. The only issue here is that you must maintain those test instructions while making changes to the codebase. If you have added a field to the view, the regression test to check the columns on the view needs updating. Adding a bit of logic or structure to a form will mean changing the script and checking that form over.

The same goes for API calls and integrations; the expectations of the underlying code (date types and structures) will fundamentally change if you have introduced or changed an element.

DevOps tooling from Automate tests with Azure Pipelines using classic editor - Power Apps | Microsoft Learn Microsoft is your starter here, as well as Playwright Automate tests with Azure Pipelines using classic editor - Power Apps | Microsoft Learn from Microsoft. Selenium has been the go to for some years and is pretty standard across most enterprises for web testing.

This obviously adds an overhead to your dev cycle, as developers need to ensure they are communicating with the test team or maintaining the scripts themselves. Also, the time taken to run the scripts can affect how quickly a build can be pushed to production, with the knowledge that the likelihood of failure is significantly diminished when you get there.

### 6 - Enterprise Development

This is where it gets hard-core. Utilising aspects of everything, we are allowing multiple development streams, automation of development environments, and automation of code testing at the earliest stage available.

Driven by Azure DevOps or a similar CI/CD platform, a developer will initiate an environment to add a new feature. They will update the Package Deployer template to automate the deployment of that feature (if necessary). All automated unit, integration, and acceptance tests will be written before a pull request is then created for the work.

Pull requests will trigger a validation pipeline which will build and deploy the merge result of the developerâs branch with the main branch to a temporary test environment. All QA activities (including the execution of all automated tests) will happen in this environment before the feature is merged into the main branch. This ensures that every piece of work is independently regression tested and production-ready by the time it is merged. Deployments can happen to production anytime by taking any build from the main branch. Multiple releases can be supported easily with hotfixes as temporary environments can be created based on builds released into any environment (e.g. UAT or prod).

At the far end of the ALM scale, the time and cost for this structure is significant. A DevOps expert will be required to create and maintain the pipelines. With validation in every PR, you add a time delay for the developer on checkin. You will also have a cost of the pipeline runs, and provisioning new environments can be expensive if you are at your user limit. These factors make this version only applicable to the mission critical projects, with numerous moving parts, to ensure the investment required can be recognised against the reduced risk of bugs creeping in.

## Summary

As you can see, there is a spectrum of options available to anyone considering developing solutions and managing their deployment. From none to a full suite of automation and testing, allowing multiple developers, multiple work streams, and full regression testing.

Whilst there is never going to be a one-size-fits-all when it comes to CI/CD, I hope I have given you some thoughts to consider.

This diagram consolidates all the considerations in one place. This really highlights how your thinking should be evolving as your application becomes more critical to your organisation.

Special thanks to Max Ewing. He is the talent here. Max is a Senior Software Engineer at Capgemini and delivers Enterprise CI/CD for numerous clients. His continued push to improve the quality of our deliveries is beyond exemplary.