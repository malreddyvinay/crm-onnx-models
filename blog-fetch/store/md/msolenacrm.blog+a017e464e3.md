In my world being an expert in something and being a dummy in something else is pretty normal. No one knows everything. I am an expert in the Power Platform and Business Applications, but even that area is too big for me, so I continue learning every day.

When I tried to deploy the Power Platform communication site template for my organisation, I encountered multiple issues. They look like silly issues to me now and I am sure 99.9% of you would never struggle with something like this. But I did.

First, I am not a PowerShell expert. Over the past year, I have learned that being a good developer doesn’t necessarily make you a good administrator. So it’s okay; I’ll keep learning.

Second, being a Power Platform expert doesn’t automatically make you an Office 365 expert. The SharePoint world has changed since I was a SharePoint developer, so there are things to learn here as well.

Third, I always remember that if I struggle with ‘stupid things,’ someone else in the world is likely experiencing the same issues. So I am happy to share my learning with you. Perhaps it will save you some time.

## Create an internal Microsoft Power Platform hub

At the heart of growth is a community, a place for people to collaborate, share ideas, and discover new ways to apply technology to achieve more. A community is a safe place to ask questions to share tacit knowledge and expand skill sets. Organizations that have succeeded at creating a growing community of makers provide tools such as Yammer or Microsoft Teams groups, regular events and speaking opportunities, and foster an environment of ongoing learning.

They make sure that every person in the organization can come together at regular intervals to socialize, share their knowledge, and explore new possibilities. Leaders who want to create a digital culture will put a framework in place for the community inside their organization to break down geographic and organizational silos.

…

Set up your own SharePoint Hub or Teams site to share success stories, upcoming events, rules of engagement, and guidelines with your maker community – or get started with the Power Platform Hub template. This site should be a one-stop shop for makers to find out everything they need to get started with Microsoft Power Platform.

Microsoft Learn

## Get started with the Power Platform communication site template

We start with Microsoft Learn, here you will find very good step-by-step instructions:

Good enough for someone who’s not me 😎 Therefore, issue number 1.

## Issue 1. The incorrect version of PowerShell running on your machine.

When you download a zip file from here: https://aka.ms/pphub-download and extract it, you will see the template file and two PowerShell script files inside.

We need to download and install **PnP PowerShell** to run the **Deploy-PowerPlatfromHub** script and **Microsoft.PowerApps.Administration.PowerShell** to run **PowerPlatformHubAsDLPErrorSettings** script.

In the documentation, we find the following statement:

The PowerShell commands in the Microsoft.PowerApps.Administration.PowerShell module requires Windows PowerShell version 5.x.

Microsoft Learn

It’s somehow misleading as it only mentions the PowerShell version requirements for **Microsoft.PowerApps.Administration.PowerShell** module. It says nothing about PnP PowerShell.

What’s PnpPowerShell?!

PnP PowerShell is a .NET Core 3.1 / .NET Framework 4.6.1 based PowerShell Module providing over 600 cmdlets that work with Microsoft 365 environments such as SharePoint Online, Microsoft Teams, Microsoft Project, Security & Compliance, Microsoft Entra ID, and more.

For more information about installing or upgrading to this module, refer to these PnP PowerShell articles.

Microsoft Learn

Is PowerShell version 5.x. mentioned in the article good enough? Let’s see!

From the PnP PowerShell website, not the original article!

You need PowerShell 7.2 or later to use PnP PowerShell. It is available for Windows, Linux and Mac and can be installed through here.

https://pnp.github.io/

What a pleasant surprise!

Check the version of PowerShell running on your machine:

`$PSVersionTable.PSVersion`
Update if required:

## VSCode to Debug

If you run the script and everything worked the first time, don’t read any further. This article is for people like me, people who ran the script and it failed.

My **Deploy-PowerPlatfromHub** script failed the first, the second, and third time. To debug I decided to load the script to VSCode which makes it easy to debug.

## The Script

The script is pretty straightforward. When you know 😁

There is some code but most of it is just an error handling and some checks.

All it does is create a SharePoint site and then import the template.

This is the bit you have to get right. It looks pretty straightforward yet I made a mistake.

```
$adminTenantName = 'contoso'
$adminURL = 'https://' + $adminTenantName + '-admin.sharepoint.com'
$companyName = 'Contoso'
$lcid = 1033
$newSiteURL = 'https://' + $adminTenantName + '.sharepoint.com/sites/powerplatformhub'
$ownerEmail = 'owner@contoso.com'
$siteTemplate = 'SITEPAGEPUBLISHING#0'
$siteTitle = 'Power Platform Communication Site'
$timeZone = 2
```
But I will talk about it later in the section **Issue 4. Timezone parameter.** 

## Issue 2. ‘PowerShell Script Is Not Digitally Signed’

During my script execution attempts I was getting the error message ‘PowerShell Script Is Not Digitally Signed’ multiple times.

Read the article below to understand the issue.

https://codesigningstore.com/powershell-script-is-not-digitally-signed-error

The “PowerShell script is not digitally signed” message is the outcome of one of Microsoft’s already built-in security features. The protection is based on the script execution policies regulating which scripts are allowed to run on your computer.

https://codesigningstore.com/powershell-script-is-not-digitally-signed-error

I tried different things as suggested here and in other blog posts.

What helped me personally is the following:

Untick the **Unblock** tickbox on the General tab of the script file Properties then click OK.

## Issue 3. The SharePoint site hasn’t been provisioned correctly

Remember I told you I got my parameters wrong? It’s time to explain what happened.

When I ran the script, still the first one, it created a site. Unfortunately, the site hasn’t been provisioned correctly. I didn’t know about it as I didn’t get any errors about the issue.

Which is pretty unusual counting everything I described above 😁

When I clicked on the site link, it displayed an error.

## Issue 4. A Timezone parameter

Where would you get the Timezone parameter?

```
$adminTenantName = 'contoso'
$adminURL = 'https://' + $adminTenantName + '-admin.sharepoint.com'
$companyName = 'Contoso'
$lcid = 1033
$newSiteURL = 'https://' + $adminTenantName + '.sharepoint.com/sites/powerplatformhub'
$ownerEmail = 'owner@contoso.com'
$siteTemplate = 'SITEPAGEPUBLISHING#0'
$siteTitle = 'Power Platform Communication Site'
$timeZone = 2
```
I found somewhere on the Internet. WRONG!

`Get-PnPTimeZoneId`
In order to create a new classic site you need to specify the timezone this site will use. Use the cmdlet to retrieve a list of possible values.

https://pnp.github.io/

## Issue 5. The template file path

Who likes 404? I do!

In the script part below replace **template.pnp** with whatever you like either a relative path if you are a very smart person or an absolute path if you are like me.

```
 ## Import Template
      Invoke-PnPSiteTemplate -Path template.pnp -Parameters @{'CompanyName' = $companyName; 'Year' = $year; 'Month' = $month } -ErrorAction Stop
```
It will be something like this:

```
## Import Template
      Invoke-PnPSiteTemplate -Path "C:\PowerPlatformHub\template.pnp" -Parameters @{'CompanyName' = $companyName; 'Year' = $year; 'Month' = $month } -ErrorAction Stop
```
Finally! The first script was successfully executed and the second one only had one error which is ‘PowerShell Script Is Not Digitally Signed’ and was easy to fix.

The result is below. Looks A-M-A-Z-I-N-G!

Wait a second! Where is my navigation?!

## Issue 6. The site doesn’t have a navigation

Well… last time we installed it at a client it somehow fixed itself the next day 🤔

This time I didn’t want to wait for the miracle to happen.

From the top menu **Settings** -> **Change the look**

Click on the **Navigation**.

Site navigation visibility toggled on. Save.

From the top banner click on **Edit**.

Enable site navigation audience targetting toggle on. Save.

Ta-a-da-a!

The template is great! it has the foundation of everything you need to communicate with makers. I want you to love it as much as I do. Therefore if you experience any issues with the deployment of the hub let me know and I will try to help.

## Leave a comment