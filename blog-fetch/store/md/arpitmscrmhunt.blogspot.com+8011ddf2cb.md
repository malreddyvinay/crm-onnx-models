**Introduction**

**Hello Everyone,**

Today in this 

**Power Guide Mentorship Program**, I am going to share**#PowerGuideTip24**, which will help you to Automate the Dynamics 365 and Power Platform Deployment using Azure DevOps CI/CD.
I have already been delivered a session on 

**Dynamics 365 Azure DevOps Implementation in Dubai Submit, Feb 2020.**You can find the recordings and Slide Deck of the session**here.**
I have also delivered Power Community Session recently on - 

**Automate the PowerApps Portal Deployment using Azure DevOps CI/CD.**You can find that session recording**here.**
If you are new to Dynamics 365 and Azure DevOps, I would recommend you to first listen and go through my above-mentioned recordings and slide deck. This will help you to know the 

**Fundamentals of Azure DevOps and CICD.**
Today, In this article. I am going to share the end to end steps to implement Azure DevOps and CI/CD to automate the Dynamics 365 and Power Platform Components.

**Business Requirement**


Automate Dynamics 365 Solution, Power Platform, and Configuration Data Deployment


**Pre-Requisites**

- Dynamics 365 Source Instance - Dev
- Dynamics 365 Target Instance - SIT/UAT/PRE-PROD/PROD
- Azure DevOps Subscription - Can create trial using this **link**  and refer to**this article** for instructions
- Azure Subscription - for Dynamics 365 Service Connection - Can use the trial as well
- Need to have a solution available in your Dynamics 365 Source Instance
- Need to have some configuration (Master) data available in your source instance
- Dynamics 365 Instance (Source and Destination both) Administrator rights
- Schema File Available - if you want to deploy master data or portal configuration as well.

**Implementation Flow**

**Implementation Steps**


**Repository Permissions**


There is some security to set up to allow our pipeline to be able to upload the configuration to source control. We need to allow the 

**Project Collection Build Service**to have contributed access to the repository.
1. Click the Gear Icon in the bottom left corner to get access to **Project Settings**
2. Choose **Repositories**
3. Click on the **Permissions** tab
4. Search **Project Collection Build Service**
5. Add the **Project Collection Build Service**
6. Once you have added the Project Collection Build Service, choose **“Allow”** on the **Contribute Permission.** (from the Right panel)
7. Now Search **Build Service user** (Project Name + “Build Service”)
8. Change **Contribute** to “Allow”


**Create a CI (Build) Pipeline -**

After the Azure DevOps service is set up for your organization, create a new Azure DevOps project by clicking on 

**'+ New project'.**


Click on

**'+'**and search**Power Platform Build Tools**and Hit**'Get it Free'**
Once the Installation of the Tool is finished in your Azure DevOps instance. Search 

**Power Platform Tool Installer**task and click on**Add**
To do that, you have two choices of Authentication Type:


**(a) Username/password (no MFA support) -**In this Authentication Type,

**y**ou'll have to provide the username and password in order to make the connection with your CRM instance, however, it doesn't support two-factor or Multi-Factor authentication.

So if you want to connect the CRM Instance using username and password. Here is the format of the connection string

**Connection String Format:**

AuthType=Office365; Url=https://powerguide.crm11.dynamics.com; UserName=arpit@powerguide.onmicrosoft.com;Password=Pass@word1

**Note:**Replace the red part with your CRM Instance details.

Check my 

**this**article for more details.


**(b)**

**Service Principal/Client Secret (supports MFA) -**In this Authetication Type, you'll have to perform two steps to complete the authetication

- **__Azure App Registration__**

- To register an App in Azure, follow my **this** article. Go to the '*Azure AD App Registration'* section and perform**Step 1 to Step 6.**
- In Step 7, instead of clicking on Microsoft Graph, click on **Dynamics CRM** and Opt**User_Impersionation** Permission and then Hit**Add Permission.**
- **Step 8** will remain the same.
- One additonal step is to capture the **Azure AD Tenant ID** as well for later use

- If you find any trouble performing the above steps. Please watch this video.

- After performing all the above steps. Don't forget to Capture the Application ID, Client Secret Key and Azure AD Tenant ID for later use.

- **__Application User Creation in Dynamics 365 Source Instance__**

- Go to https://make.powerapps.com > Choose your environment > Click on **Advanced Setting**

- Go to Security > User > Select **Application Users** View > Click on**New**

- Choose **Application User** form and fill User Name, Application ID, Full Name and Primary Email (as highlighted below) and Hit**Save.**

- Once you save the record**, Application ID URI** and**Azure AD Object ID**  will get automatically autopopulated from your Azure Tenant
- Give **System Administrator** Security Role to the user.

Once you are done with 

**Azure AD App Registratio**n and**Application User Creation**, It's time to make the**Service Connection**in your Azure DevOps.
To do that, Hit on 

**+New**to create a new Service Connection for your Dynamics 365 Dev Instance
Fill the details as shown below and Hit 

**Save.**

**Command Line**task

echo commit all changes

git config user.email "arpit.crmconsultant@gmail.com"

git config user.name "arpit.crmconsultant@gmail.com"

git checkout master

git add --all

git commit -m "solution init"

echo push code to new repo

git -c http.extraheader="AUTHORIZATION: bearer $(System.AccessToken)" push origin master

**Note: Replace the highlighted username with your Azure DevOps User Account Name**

**Publish Artifacts**Task in order to push your solution zip file to the

**Artifacts.**Fill the details as shown below

Create a Variable to hold Solution Name. This variable name, we have already been used '

**$(SolutionName)'**in all the above steps.

If you want to trigger this Pipeline as soon as you commit the changes to your Master Repository, Choose 

**Enable Continous Integration.**Or you can schedule the pipeline to be run at a specific time as well.
You can opt for 

**Enable System Diagnostic**to log/troubleshoot the error in case you face any issues while running the pipeline.
**Repository**> Solution Zip file has been extracted to multiple files based on solution components

**Create a CD (Release) Pipeline -**


Click on 

**Releases**under Pipeline and**click on****+New release pipeline**in order to create the Release Pipeline.

Click on 

**Trigger Icon**and Turn On the**Enable Continous deployment**trigger (as shown below)
**Stages**in order to add the Tasks to import the solution in your Target Dynamics 365 Instance.

To do that, click on

**Empty Job**
Add 

**Power Platform Solution Import**Task and Fill the details as shown below
**Note:**You need to create a new Service Connection in order to connect with your Target Dynamics 365 Instance, same as the steps we have performed earlier to connect the Source Dynamics 365 Instance.

**Solution Input File**path. Click on Browse and choose the pah as per below and Hit

**Ok.**

Declare the Variable for Solution Name (like we did in Build Pipeline)

**Save**the Pipeline

**Watch this Video of CI and CD Pipeline Setup and Demo**

If you find any difficulties to understand any of the above steps, you can watch this video to set up your pipeline

**Deploy Dynamics 365 Master Data (or Portal Configuration Data) using Azure DevOps CI/CD**

While working in Dynamics 365, you might need to use some master data in your Dynamics 365 Instance, that remains unchanged in all the instances (Dev/SIT/UAT/PROD, etc). For Example Country, State, City, etc.

In PowerApps Portals also, everthing we do in order to design the Portal is part of configuration only. We create records in Dynamics 365 like Web Pages, Entity Forms, Entity List, Web Template, etc. Hence, this configuration is also kind of Master data because it also remains unchanged in all the target instances as well

In order to deploy above both types of configuration data in your target instance, we usually use the 

**Configuration Migration Tool**. However, that is a manual activity.
To automate the configuration data using Azure DevOps CICD, please perform the following steps:

**Important Note:**

**1.**I have created separate CI/CD Pipelines for Configuration Data Deployment, however, you can use a single CI and CD Pipeline also in order to deploy your Dynamics 365 Solution and Configuration Data in the target instance. (based on your business needs).

**2.**Currently Microsoft't Power Platform Build Tools doesn't provide the capabilities to Export/Import the Configuration records/data from/to CRM. Hence, we'll use

**Wael Hamze's Power DevOps Tools**for this requirement.

**3.**Please have a look my

**this**article, where I have demonstrated the PowerApps Portal CI/CD Pipeline creation using Azure DevOp.

**Create Repository -**


 I have created a Repository to store the Schema File. You can reuse the same repository that we have created in the earlier step. Schema file contains the list of all entities, those records have to be exported from the Source Dynamics 365 Instance.

If you are deploying the PowerApps Portal configuration. You can get the Portal Schema File from 

**here**. If it doesn't work due to any reason, you can create your own schema file as well for the selected Portal Entities.
**Create a new Repository and Create a new Folder 'Portal Configuration' inside it.**


**Create a CI (Build) Pipeline -**


Create a new Build (CI) Pipeline to export the Dynamics 365 Configuration (Master) Data



**Install Power DevOps Tools**



Add 

**Power DevOps Tool Installer**Task and leave it as is.
Add 

**Ping Environment**Task
**Note:**This tool doesn't allow to use of the Service Connection like the way we had used in Power Platform Build Tools. However, you can use the following connection string to make the connection with your Dynamics 365 Source Instance.

Application ID and Client Secret of Source Dynamics 365 Instance, we have already been captured in the earlier steps.


Add 

**Export Configuration Migration Data**Task. Browse to the**'Portal Configuration' folder in the Repository and select the Schema file.**
**Note:**

**It's always a good practice to keep the confidential information like username, password, client id, secret key in variables and enable the security so that it couldn't be comporomised.**


**Publish Artifacts**Task

Publish Artifacts is required to push the exported 

**data.zip**file to Build Artifacts.
**Note:**Make the variable value confidential by clicking on

**Lock**Icon (scroll roght)


**Create CD (Release) Pipeline -**

Configure Release Pipeline 

**Artifacts Location**and**Trigger Point**

**Power DevOps Tool Installer**Task and leave as is.


Add 

**Ping Environment**Task and Fill the details as per below
**Import Configuration Migration Data**Task and Fill the details as per below

Make the variable value confidential by clicking on 

**Lock**Icon (as shown below)
**Video of CI/CD Pipeline Setup -**

**Hope this article helps you make your Dynamics 365 Deployment process smooth and automatic. Please do share your feedback. Cheers**

Amazing. Thanks Arpit Great job. I wonder always by your every blog.

ReplyDelete
Very detailed information worth the time reading, This would be of great help to someone using crm and contact manager app.

ReplyDelete
Appreciate for the great tips listed in the article .Nice presentation and teaching I really enjoyed it .Thanks this is straight forward and to the point. This was some awesome information on Windows versions.

ReplyDelete
Thanks for providing such an awesome blog regarding azure cloud migration services. It is a very useful blog for others to read and know the information.

ReplyDelete
azure cloud migration services

This is a very amazing post for Power Automate. In this post, you have provided all the basic information regarding This. Thanks For sharing with us.


ReplyDelete
Visit: Automated Daily Activity Reports

You should mainly superior together with well-performing material, which means that see it: compro cupo dolares


ReplyDelete
Nice blog! Blog is very informative and useful for everyone. BRJ provides completely secure and reliable

ReplyDeleteCRMSoftware, has gained enough attention from the best industry experts and is still performing efficiently in providing one-stop solutions to various small and medium sized business houses.

ReplyDelete
Techforce services is a Salesforce Consulting Services in Australia Specialising in delivering end to end Salesforce solutions ,Consulting, Implementation DevOps partners in australia We deliver applications and services more rapidly and reliably, but it’s more than a methodology – it cuts to the very core.Salesforce Data Analytics let us help you become a data driven organisation and ensure your data is working hard for your business This includes implementi

Techforce services in Australia

Salesforce Consulting Services in Australia

Salesforce Staff Augmentation in Australia

Salesforce Data Analytics

DevOps Partners in Australia

Managed Projects Salesforce Australia

There are some organizations that require particular skills in cloud computing like development skills whereas others search for cloud infrastructure specialists...

ReplyDelete
devops services

Marvellous blog and articles.Directly I am found which I truly need. please visit our website for more information about Azure DevOps Services and Solutions


ReplyDelete
Merely a smiling visitant here to share the love (:, btw outstanding style. top software tools for writers


ReplyDelete