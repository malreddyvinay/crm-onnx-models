In this blog, we will see how to export and import the Dynamics 365 CE solution using the PowerShell script.

In my PowerShell script, I am using Microsoft.Xrm.Data.Powershell.

`InstallRequiredModule`
This function will check for this module (Microsoft.Xrm.Data.Powershell) in your machine. if not present then it will install this module

`EstablishCRMConnection`
This function will establish the connection to the CRM by passing the Dynamics 365 CE instance URL, username and password.

Before running the PowerShell scripts please make sure you have updated the below values.

```
$solutionName ="BuildAutomation"
$SolutionFilePath="C:\Users\DBALASU\Source\Workspaces\BuildAutomation\BuildAutomation.Solutions\BuildAutomation"
$CRMSourceUserName=""
$CRMSourcePassword=""
$CRMDestinationUserName=""
$CRMDestinationPassword=""
$CRMSourceUrl="https://instancename.crm.dynamics.com"
$CRMDestinationUrl="https://instancename.crm5.dynamics.com"
```
1. $SolutionName – Name of the solution which you want to export the source instance.
2. $SolutionFilePath – Desired folder path to export the solution
3. $CRMSourceUserName – Username of the Dynamics 365 CE source instance
4. $CRMDestinationUserName – Username of the Dynamics 365 CE destination instance
5. $CRMDestinationPassword – Password of the Dynamics 365 CE destination instance
6. $CRMDestinationPassword – Password of the Dynamics 365 CE source instance
7. $CRMSourceUrl – URL of the Dynamics 365 CE source instance
8. $CRMDestinationUrl – URL of the Dynamics 365 CE destination instance.

After updating the values in the below script, you can copy and paste in Windows PowerShell and run it. This will establish the connection to the Dynamics 365 CE source instance and export the solution mentioned and import it into the Dynamics 365 CE destination instance.

```
$solutionName ="BuildAutomation"
$SolutionFilePath="C:\Users\DBALASU\Source\Workspaces\BuildAutomation\BuildAutomation.Solutions\BuildAutomation"
$CRMSourceUserName=""
$CRMSourcePassword=""
$CRMDestinationUserName=""
$CRMDestinationPassword=""
$CRMSourceUrl="https://instancename.crm.dynamics.com"
$CRMDestinationUrl="https://instancename.crm5.dynamics.com"
Set-StrictMode -Version latest
function InstallRequiredModule{
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
$moduleName = “Microsoft.Xrm.Data.Powershell”
$moduleVersion = “2.7.2”
if (!(Get-Module -ListAvailable -Name $moduleName )) {
Write-host “Module Not found, installing now”
$moduleVersion
Install-Module -Name $moduleName -MinimumVersion $moduleVersion -Force
}
else
{
Write-host “Module Found”
}
}
function EstablishCRMConnection{
param(
[string]$CRMUserName,
[string]$CRMSecPasswd,
[string]$crmUrl)
Write-Host "UserId: $CRMUserName Password: $CRMSecPasswd CrmUrl: $crmUrl"
$CRMSecPasswdString = ConvertTo-SecureString -String $CRMSecPasswd -AsPlainText -Force
write-host "Creating credentials"
$Credentials = New-Object System.Management.Automation.PSCredential ($CRMUserName, $CRMSecPasswdString)
write-host "Credentials object created"
write-host "Establishing crm connection next"
$crm = Connect-CrmOnline -Credential $Credentials -ServerUrl $CrmUrl
write-host "Crm connection established"
return $crm
}
InstallRequiredModule
#Update Source CRM instance details below:
Write-Host "going to create source connection"
$CrmSourceConnectionString = EstablishCRMConnection -user "$CRMSourceUserName" -secpasswd "$CRMSourcePassword" -crmUrl "$CRMSourceUrl"
Write-Host "source connection created"
Set-CrmConnectionTimeout -conn $CrmSourceConnectionString -TimeoutInSeconds 1000
Write-Host "going to create destination connection"
$CrmSourceDestinationString = EstablishCRMConnection -user "$CRMDestinationUserName" -secpasswd "$CRMDestinationPassword" -crmUrl "$CRMDestinationUrl"
Write-Host "destination connection created"
Set-CrmConnectionTimeout -conn $CrmSourceDestinationString -TimeoutInSeconds 1000
Write-Host "Publishing Customizations in source environment"
Publish-CrmAllCustomization -conn $CrmSourceConnectionString
Write-Host "Publishing Completed in source environment."
Write-Host "Exporting Solution"
Export-CrmSolution -conn $CrmSourceConnectionString -SolutionName "$solutionName" -SolutionFilePath "$SolutionFilePath" -SolutionZipFileName "$solutionName.zip" 
Write-host "Solution Exported."
Write-host "Importing Solution"
Import-CrmSolution -conn $CrmSourceDestinationString -SolutionFilePath "$SolutionFilePath\$solutionName.zip"
Write-host "Solution Imported"
Write-Host "Publishing Customizations in destination environment"
Publish-CrmAllCustomization -conn $CrmSourceDestinationString
Write-Host "Publishing Completed in destination environment"
```
I hope this helps.

If you are interested in this topic and would like to do some further self-study I encourage you to check out my blog on this.

Reblogged this on Let Us Discuss and commented:

Thanks to Dharani for yet another awesome blog on build automation. Hope this will be helpful for all D365 enthusiasts.

LikeLike

Hi, i am unable to run the very first line “Microsoft.Xrm.Data.Powershell” says it is not recognized, am i missing some prerequisite here?

LikeLike

Import-Module Microsoft.Xrm.Data.Powershell

LikeLike