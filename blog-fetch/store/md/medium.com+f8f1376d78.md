# Migrate Dynamics CRM 365 On-Premise to CRM 365 Online

**Pros of Migrating to Dynamics 365 Customer Engagement (CE) Online:**

• Cost reduction: Moving to Dynamics 365 CE Online can help reduce costs associated with maintaining on-premises infrastructure and resources.

• No manual upgrades: Microsoft handles all upgrades and maintenance for Dynamics 365 CE Online, so you don’t have to worry about performing manual updates.

• Fewer resources needed: Migrating to Dynamics 365 CE Online allows you to manage the system with fewer resources, including infrastructure and database expertise.

• High availability and disaster recovery: Dynamics 365 CE Online offers a high availability and disaster recovery environment, with a guaranteed 99.9% uptime by Microsoft.

• Greater support: Microsoft provides more support for product issues with Dynamics 365 CE Online compared to the on-premises version.

• Access from anywhere: Dynamics 365 CE Online can be accessed from any location with an internet connection.

• Office 365 integration: You can use your Office 365 ID for login and multi-factor authentication (MFA) with Dynamics 365 CE Online.

• Multiple device access: Dynamics 365 CE Online can be accessed using a variety of devices, including mobile phones and tablets.

• Email tracking with Outlook: You can use the Outlook App to track emails with Dynamics 365 CE Online.

• Access to online features: Dynamics 365 CE Online provides access to Microsoft CRM online features and technologies, such as Power Apps, Flows, and Power BI.

**Limitations of Dynamics 365 Online:**

• Cannot use third-party DLLs for plugin and workflow development, which may limit the functionality that can be added to the system.

• Reports can only be developed using fetch xml, which may not be suitable for all reporting needs and may require additional time and effort to convert existing SQL reports.

• Additional data storage and attachment storage may be required at an additional cost, depending on the size and usage of the system.

• Extra testing and releases may be necessary for regular CRM rollup upgrades to ensure that the system continues to function as expected and to address any potential issues that may arise.

• There is limited control over the infrastructure and hardware, which is managed by Microsoft. This means that the organization may not have the ability to make certain customizations or configurations to the system.

**Using Dynamics 365 On-Premise:**

• The organization has full control over the environment and can make unsupported customizations to the system.

• The organization has full control over the database and can develop SQL reports and write SQL queries for data extraction.

**Limitations of Dynamics 365 On-Premise:**

• Requires more cost, infrastructure, and staff to manage the system.

• May require specialized application experts to manage the infrastructure, such as ADFS, SSRS, and SQL DBA (Cluster, Always On with DR).

• Regular maintenance is required, including OS and security patches, which may require downtime and regression testing.

• Vulnerability scans and penetration testing may be necessary, with necessary fixes required to address any identified issues.

• Support from Microsoft may be more difficult to obtain and may take longer to resolve issues compared to the online version of Dynamics 365.

**Dynamics 365 V8 (on-Prem) vs Dynamics 365 CE (online)**

**Technical differences**

• Dynamics 365 CE Online is entirely cloud-based and managed by Microsoft (including product, database, data center, and infrastructure)

• CRM rollup upgrades are managed by Microsoft twice a year.

• Database, data center, and disaster recovery (DR) managed by Microsoft (DB backup and restoration is very fast and simple)

• Reports — Only supports Fetch XML reports, not SQL query reports, it might be required to convert SQL based reports before online migration.

• Interfaces with other systems — Requires opening of firewall connections to connect to other systems.

• Does not support Outlook client, requires switch to CRM Outlook online app

• Incompatible JavaScripts may need to be modified for new XRM APIs.

• ADFS server not required, can use Office 365 login ID for authentication

• Plugins and workflows using third-party DLLs must be modified (Ex: IL merge)

**Requirements**

• User training on new system and change management process during testing (UAT)

• Personalized experience apps based on CRM security roles for improved access management and ease of use (e.g. back office app, admin app, shop ops app)

• UI changes with Dynamics 365 CE Online 9.1 using unified client interface (UCI)

**Operations**

• Rollup version upgrades: It is important for users of Dynamics 365 CE Online to be aware of and plan for rollup version upgrades, which are managed by Microsoft and occur twice a year. Users should be informed of the changes and asked to try them out in the testing environment (UAT). All versions of the system (development, staging, testing, and production) must be upgraded to the same rollup.

• Maintenance and downtime: There is no need for a system maintenance window or downtime with Dynamics 365 CE Online, as the system is managed and maintained by Microsoft.

• Accessibility: Dynamics 365 CE Online can be accessed from anywhere in the world, which allows users and the development team to work remotely and provide better support.

• User experience: The user experience may be different in Dynamics 365 CE Online due to changes in the unified client interface (UCI).

• Microsoft support: Microsoft support is generally more available for Dynamics 365 CE Online compared to Dynamics 365 V8 On-Premise.

• New features: Users of Dynamics 365 CE Online receive new features twice a year as part of the rollup updates.

**Migration Plan**

**Assumptions**

• Eligibility for FastTrack migration: The company has the necessary eligibility requirements for FastTrack migration.

• Migration method: The migration will be done using the FastTrack method.

• Account type: Hybrid AD accounts will not be used, and Office 365 accounts will be used to access the system.

• Email address and profile: The email address will be an Office 365 account and the email profile will be configured using Microsoft Exchange Online.

• Deployment server and organization: A new deployment server with Windows Server 2016 and SQL 2016 will be set up to create a separate organization for customizations required for CRM Online migration. The current server and organizations should not be used to avoid impacting current operations.

• Azure Tenant: The company has an Azure Tenant, and an Azure subscription and storage account (which the customer will need to pay for along with Dynamics 365 subscriptions) have been set up, along with provisions for two sandbox environments in staging.

• CRM licenses: All necessary CRM licenses have been purchased before the migration.

• Microsoft Lifecycle Services: The migration project has been set up in Microsoft Lifecycle Services, which uses a wizard-based hosted tool for the migration. Microsoft Lifecycle Services

• Managed CRM solution: A managed CRM solution will be used for deployment to the testing and production environments.

**Here are some points to consider** when planning a migration to Dynamics 365 Customer Engagement (CE) Online:

• Dual licenses: It is possible to use a Dynamics 365 CRM On-Premise license for the online version of the software.

• Licensing method: The most cost-effective licensing method can be chosen based on the client’s budget and system access requirements. Options include Enterprise (more costly), Power app (less costly), and Team Member (less costly).

**Setup Development Environment**

Here is a list of steps to set up a development environment for a migration to Dynamics 365 Customer Engagement (CE) Online:

• Set up a new on-premise server: A new server should be set up using the development environment before creating an online migration solution to avoid additional migration cycles. This server should have CRM V8, SQL 2016, and the operating system Windows Server 2016.

• Create a new development organization: A new development organization can be created by restoring the existing development CRM database and importing the organization.

• Make necessary changes in the development CRM: The following changes should be made in the development CRM:

*• Create a new CRM solution and include all customizations in that solution*

*• Convert SQL-based reports to Fetch XML*

*• Update plugins and workflows to run in sandbox mode*

*• Check for and reconfigure any integration with third-party tools, and remove IL merge*

*• Update JavaScript to the new client object model (compatible with the unified client interface (UCI))*

*• Update CRM forms to provide a rich user experience with the UCI*

*• Make the solution online compatible*

*• Test that all application functionalities are working as expected*

• Upload the database backup to Azure Blob Container: Take a database backup, log in to the Lifecycle portal, and upload the database backup to the Azure Blob Container.

• Upgrade CRM: Follow the steps to upgrade CRM 9.0, then CRM 9.1, using the provided tools and steps.

• Validation of the migration: Run the validation report and fix any issues identified in the CRM V8 environment. Once the issues are fixed, upload the database backup again, follow the same steps, and ensure that the validation report is successful before uploading the CRM online via the Lifecycle portal.

• Creation of the online development environment: Once the validation steps are completed, follow the steps in the Lifecycle portal to create the CRM Online development environment.

• User mapping: Upload user mapping with the permissions required to complete the migration successfully.

• Regression testing in the online environment: Perform testing in the online environment to ensure that all functionalities are working as expected. This may include functional, integration, and user acceptance testing.

**Setup UAT Environment**

Here are the steps to set up a testing (UAT) environment for a migration to Dynamics 365 Customer Engagement (CE) Online:

• Create a new UAT organization: A new testing organization can be created by restoring the existing testing CRM database and importing the organization in the new environment.

• Import the customized solution from the development CRM: Import the customized solution from the development CRM to the testing environment, including any fixes made during the development migration.

• Upload the database backup to Azure Blob Container: Take a database backup, log in to the Lifecycle portal, and upload the database backup to the Azure Blob Container.

• Upgrade CRM: Follow the steps to upgrade CRM 9.0, then CRM 9.1, using the provided tools and steps.

• Validation of the migration: Once issues are fixed, upload the database backup again, follow the same steps, and ensure that the validation report is successful before uploading the CRM online via the Lifecycle portal.

• Creation of the online testing environment: Once the validation steps are completed, follow the steps in the Lifecycle portal to create the CRM Online testing environment.

• User mapping: Upload user mapping with the permissions required to complete the migration successfully.

• Testing: Perform a full regression test to ensure that all functionalities are working as expected in the online testing environment. This may include functional, integration, and user acceptance testing.

• Familiarization with the new unified client interface: Help users become familiar with the new unified client interface (UCI).

**Setup Production Environment**

Here are the steps to set up a production environment for a migration to Dynamics 365 Customer Engagement (CE) Online:

• Pilot migration: Microsoft can provide support for a pilot migration before the production CRM migration in the new environment.

• Inform users: Inform users that they will need to stop using the production system.

• Create a new production organization: A new production organization can be created by restoring the existing production CRM database and importing the organization.

• Upload the database backup to Azure Blob Container: Take a database backup, log in to the Lifecycle portal, and upload the database backup to the Azure Blob Container.

• Validation of the migration: Once issues are fixed, upload the database backup again, follow the same steps, and ensure that the validation report is successful before uploading the CRM online via the Lifecycle portal.

• Creation of the online production environment: Once the validation steps are completed, follow the steps in the Lifecycle portal to create the CRM Online production environment.

• User mapping: Upload user mapping with the permissions required to complete the migration successfully.

• Testing: Perform a full regression test to ensure that all functionalities are working as expected in the online production environment. This may include functional, integration, and user acceptance testing.

**Eligibility**

FastTrack assistance is available for customer tenants with 150 or more licenses from one of the eligible plans from the following Microsoft product families: Microsoft 365, Office 365, Microsoft Viva, Enterprise Mobility & Security, and Windows 10. However, it may still be possible to get Microsoft support by talking to them and convincing them of the future usage of the online CRM system and the increase in user licensing capacity.

Have you migrated Dynamics 365 Online to On-Premise? Share your experience in the comments below.

More Information: https://docs.microsoft.com/en-IN/fasttrack/eligibility

Dynamics CRM (on-premises) to Dynamics 365 migration — Dynamics 365 | Microsoft Learn