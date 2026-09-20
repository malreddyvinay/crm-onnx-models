*Overview*

It is no longer in question if any organization planning to enhance productivity and scalability should utilize cloud-enabled technologies. It was so rewarding for me to assist one of my customers in migrating their MS Dynamics CRM on premises system with data into Dynamics 365 CRM Online.

My customer had been using the MS Dynamics CRM on-premises version for years, but with evolving technological needs and the desire for improved accessibility, they opted to migrate to MS Dynamics 365 CRM Online. With this shift, they would be better able to integrate other Microsoft cloud services, receive enhanced security, and have scalable systems and solutions.

In this blog, I specifically talked about the data migration activities, challenges, approaches, and outcomes.

*Challenges in Data Migration*

Migrating data from the Dynamics CRM on premises system to the Dynamics 365 CRM Online instance is an exceedingly complex process. A few of the challenges are:

- **Data Volume and Complexity** : The on-premises system housed years of data, including student records, admissions details, and alumni interactions.
- **Data Integrity and Cleansing** : Duplicate records, incomplete data, and inconsistencies required thorough cleansing before migration.
- **Maintaining Historical Data:** The main requirement of our customer was to maintain the same values of the following fields as we have currently in the MS Dynamics CRM on-premises.
  - Created On
  - Created By
  - Modified On
  - Modified By
  - Owner
- **Migrating Audit History:** Another critical requirement was to migrate the audit history as well.
- **Minimizing Downtime** : Ensuring a smooth transition without disrupting ongoing business operations.

*The Migration Approach*

To ensure a successful migration, we adopted a structured approach. We have divided all the tables in the following different categories.

- **Master Data** : The migration of the master data was straight forward as we don’t need to worry about to maintain the historical values of any fields like created on, created by, modified on, modified by and owner.

We have used the OOB export / import feature to migrate the master data from the Dynamics CRM on-premises to the Dynamics 365 CRM online version.

- **Transactional Data:** The real challenges was to migrate the transactional data where we need to maintain the historical values of the fields like created on, created by, modified on, modified by and owner.

To migrate the transactional data, we have used the combination of the data migration tool and the CRM plugins so that we can maintain the same historical value for the fields like “Created On” or “Modified On”. We have followed the following steps for the end-to-end data migration process.

1. We have created two new custom date fields for each entity to capture the historical date of the fields, like “Created On” and “Modified On.”
2. We have used the Configuration Migration Tool (CMT) to export the schema and data from the Dynamics On-Premises instance, map the data for the OOB Created on and Modified On with the custom fields, and migrate the data to the Dynamics CRM Online instance.
3. We have used the CRM plugins that will execute on the pre-create and read the value from the custom date fields and assign the date value to the OOB created on and modified on fields.

Below are the detailed steps.

*Prerequisites*

Before starting the migration, ensure:

✔ You have admin access to both Dynamics On-Premises and Dynamics 365 CRM Online instances.

✔ The Configuration Migration Tool is installed (part of the Dynamics 365 SDK).

✔ The schema and entity structure in Dynamics 365 CRM Online matches the Dynamics On-Premises instance.

✔ You have backed up your On-Premises CRM database as a precaution.

*Step 1: Install and Open the Configuration Migration Tool*

- Download the Microsoft Dynamics 365 SDK (if not already installed).
- Extract the SDK and navigate to:
- Tools → Configuration Migration
- Run the ConfigurationMigration.exe file (refer Fig. 1).

*(Fig. 1)*

*Step 2: Create a New Data Schema File*

Before exporting data, you need to define a schema file that specifies which entities and fields to migrate.

- In the Configuration Migration Tool, click Create Schema (refer Fig. 2).

*(Fig. 2)*

- Connect to your Dynamics On-Premises CRM (refer Fig. 3):
  - Enter the CRM URL and login credentials.
 
  - Select the On-Premises instance you want to migrate.

*(Fig. 3)*

- Select the entities to migrate (refer Fig. 4):
  - Click Add Entity and choose the required entities (e.g., Accounts, Contacts or any Custom Entities).
 
  - Expand each entity and check the fields you want to migrate.

*(Fig. 4)*

- Set lookup relationships correctly to maintain data integrity.
  - Click Save Schema and export it as a .xml file (refer Fig. 5).

*(Fig. 5)*

*Step 3: Export Data from Dynamics CRM On-Premises*

- In the Configuration Migration Tool, click Export Data (refer Fig. 6).

*(Fig. 6)*

- Select the schema file (.xml) created in Step 2.
- Choose the export destination and specify a .zip file to store the exported data.
- Click Export and wait for the tool to extract and package the data.
- Once complete, verify the data.zip file is successfully created (refer Fig. 7).

*(Fig. 7)*

- Update schema file (.xml) to replace the OOB date fields (refer Fig. 8).

*(Fig. 8)*

*Step 4: Import Data into Dynamics CRM Online*

- In the Configuration Migration Tool, click Import Data (refer Fig. 9).

*(Fig. 9)*

- Connect to the Dynamics 365 Online instance:
  - Enter your CRM URL and login credentials.
 
  - Select the target environment where data will be imported.
- Upload the exported .zip file from Step 3 (refer Fig. 10).

*(Fig. 10)*

- Click Import and wait for the data transfer to complete (refer Fig. 11).

*(Fig. 11)*

- After completion, review the import logs to check for errors or missing records (refer Fig. 12).

*(Fig. 12)*

*Step 5: Validate the Data in Dynamics 365 Online*

- Log in to Dynamics 365 CRM Online.
- Navigate to the entities you migrated and check if:
  - All records are present.
 
  - Lookup fields and relationships are intact.
 
  - Data integrity is maintained.
- Run Advanced Find queries to compare records between Dynamics On-Premises and Dynamics Online CRM.
- If issues are found, re-export and re-import the affected records.

- **Audit History Data:** Other challenges were to migrate the historical audit history from the Dynamics CRM on-premises to the Dynamics CRM online version.

As we cannot create or modify any of the records in the OOB Audit entity, we have created two new custom entities to capture and display the historical audit history from the Dynamics CRM on-premises instance to the Dynamics 365 CRM online instance. Further, we have created a console application to fetch the data. I’ll write a detailed blog to explain all the steps we followed to migrate the Audit History from the Dynamics CRM On-Premises to the Dynamics 365 CRM Online instance.

*Key Outcomes & Benefits*

The migration was a success, and the customer quickly reaped the benefits of the new cloud-based system:

- **Enhanced Accessibility** : The staff could now access CRM data securely from anywhere.
- **Improved System Performance** : The cloud-based solution ensured faster processing and better system uptime.
- **Seamless Integration** : The new system integrated well with Microsoft 365, Power BI, and other cloud services.
- **Scalability & Security** : With Dynamics CRM Online, the customer now has a scalable, secure, and easily maintainable solution for the future.

*Final Thoughts*

Migrating data from the Dynamics CRM on-premises to the Dynamics CRM Online instance is a complex but rewarding process. This project demonstrated the importance of careful planning, stakeholder collaboration, and robust data management strategies. For organizations considering a similar move, investing in a structured migration plan is crucial for a seamless transition.