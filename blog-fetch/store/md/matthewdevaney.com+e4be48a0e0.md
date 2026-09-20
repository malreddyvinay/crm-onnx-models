# How To Setup SharePoint Integration: Model-Driven Power Apps

A SharePoint document library is often the better choice for storing files in an app vs. Dataverse file storage.  The cost of SharePoint file storage is much cheaper ($0.20/GB vs $40/GB), it has versioning built-in and you can take advantage of tagging/metadata among other things.  Fortunately, we can use SharePoint to store the files for any table in a model-driven app.  In this article I will show you how to enable the SharePoint integration for model-driven Power Apps.

### 



**Introduction: The Project Tracker Model-Driven App**

Employees at a construction firm use the Project Tracker model driven app to keep important documents organized. The documents are displayed in a sub-grid and are stored inside of a SharePoint document library.

 

### 



**Create A New Model-Driven App**

Open the Power Apps maker portal and add a new table named *Project* with the following columns:

- Name (text)
- Description (text)
- City (text)
- State (text)
- Contract Amount (currency)


Populate the *Projects* table with this data:

| **Name** | **Description** | **City** | **State** | **Contract Amount** | 
| 2023-001 | Office Tower 123 River Ave. | Albany | NY | 13,500,000 | 
| 2023-002 | Strip Mall 1st St. N. | Newark | NJ | 2,300,000 | 
| 2023-003 | Big Box Store 734 Thames St | Pittsburgh | PA | 1,700,000 | 
| 2023-004 | Office Building 789 Reading Ave. | New York | NY | 89,00,000 | 
| 2023-005 | Condo Tower 1003 Main St. | Chicago | IL | 5,600,000 | 


Update the Main View of the Projects table to look like the view below:


And modify the Main Form to look like this form.

### 



**Provision A New SharePoint Team Site**

We need to setup a new SharePoint site where the model-driven app will store its documents.  Create a new SharePoint Team site.  No other configuration is required here. When we setup the SharePoint integration with the model-driven app it will be done automatically for us.

### 



**Navigate To The Advanced Settings Menu**

Now we are ready to connect our SharePoint site to the model-driven app. Go back to Power Apps and click on the gear icon in the top-right corner. Choose *Advanced Settings.*


Then select *System* > *Document Management*.


The Document Management settings menu looks like this.

### 



**Enable The SharePoint Integration With The Model-Driven App**

Next we will turn on the SharePoint integration with Power Apps.  Select *Enable Server-Based SharePoint Integration*.

Navigate past the first screen of the setup wizard.


Choose *Online* on the Define Deployment screen.


Supply the *URL* of the SharePoint site we created and press the *Next* button.


Wait for the site to become validated.  Then press *Enable.*


A success message will appear once the integration is enabled.

### 



**Choose Which Tables Use A SharePoint Document Library**

We must define which tables in our model-driven app require a SharePoint document library.  One document library will be setup per table.  To do this, open the *Document Management Settings* from the Advanced Settings menu.


Select the *Project* table.  This example uses only one table. But we do have the ability select more than one table if needed.


Select *Next* on this screen.  Do not enable *Based On Entity* unless you are using the *Account* or *Contact* tables.


At this point the SharePoint document library will be created automatically by the integration.  Wait for the process to complete.


After the the process is done we see the *document library creation status* page. The status should read *succeeded*.  Press *Finish*.

### 



**Upload A File Using The Document Associated Grid**

We can now use the model-driven app to store documents in SharePoint.  Open a the main form of any record in the Project table.  Navigate to the related *Documents* table.


The *Document Associated Grid* appears.  Choose Upload.


Choose a file to upload and press OK.


The uploaded file appears in the grid.

### 



**Locate The Uploaded Document In SharePoint**

The document we uploaded in the model-driven app is stored in a SharePoint document library. Let’s go find the document in SharePoint to understand more about the file structure being created behind the scenes.

Open the SharePoint site and go to *Site Contents*.  Navigate to the *Project* folder.


Inside the *Project folder* there will be one subfolder for each *Project* record.  Open the folder that matches the project we uploaded the document to.


Inside the folder we can see the uploaded file.

### 



**Display The SharePoint Document Library On A Main Form Tab**

It is not ideal to make model-driven app users go searching for the Documents table within the Related tab. We can make is easier for them by showing Documents on their own main form tab.

Edit the main form of the *Project* table.  Add a new 1 column tab named *Document* to the form. Insert a subgrid into the first section.  Check the *show related records* box, choose the *Documents* table and use the *All SharePoint Document* default view.


Then Save & Publish.  Ignore the warning message on the subgrid. It only appears in the editor.


When we open the model-driven app and go to the Documents tab the subgrid displays our documents.

### **Did You Enjoy This Article?**   😺

Subscribe to get new Copilot Studio articles sent to your inbox each week for FREE

### 



**Questions?**

If you have any questions or feedback about **How To Setup SharePoint Integration: Model-Driven Power Apps** please leave a message in the comments section below.  You can post using your email address and are not required to create an account to join the discussion.

Thank you for another great blog post, the detailed step by step descriptions is super useful.

Are there any considerations or drawbacks using ALM with this setup?

Cheers

Dan

Dan,

You will need to setup the integration in each environment using these steps. Solutions cannot transport this configuration. That’s all. It’s pretty simple.

Will this mean creating 3 separate document libraries in SP, one for each environment? Have confirmed this method works in the dev env (thanks Matt!) but now considering the client SP infrastructure and if the 3 separate libraries (Dev, Test and Production) will be needed. Thanks in advance

I think its only settings by tenant, not environment.

Hey Matthew! Great post as usual. Does the functionality break for you when you toggle the “Try the new look” feature in the top bar of the MDA? If yes, I think MS may have broken something. As an MVP, maybe you can let them know. Matt

Excellent blog as usual. Thanks Matthew!

A quick question: Can we upload multiple files for each Project table record or it is 1 file per record only?

Sam,

Using this method you can upload unlimited files 😊

Hi Matthew – Glad to see you’re doing all these posts on Sharepoint integrations. I wrote a similar 6-part series of some other techniques you may find interesting. In my experience, this type of thing is one of the most commonly requested functionalities.

Modern File Storage for the Power Platform (Part 1): Meta Data Tagging (mibar.net)

Andrew,

Looks neat. Thanks for the share.

FYI Andrew, I’m getting an error when I try to view your link above and even when I try to go to mibar.net

Hi Matthew, amazing post!

I was wondering if there was a way to visualise this SharePoint library items within model driven table using canvas app integration?

Raj,

This was answered in my previous post which shows how to display a document library inside of a custom page.

🔗 https://www.matthewdevaney.com/sharepoint-document-library-in-a-power-apps-custom-page/

Thanks! Any strategies or methodologies to use power automate for more advanced document management than just one folder per record within the synced document library. Or to auto update meta data based on the record context and move files using PA.

Basically I am trying to figure out the best way to blend model driven apps and sharepoint integratiom, one team site per project, and management of projects team sites and do portfolio mgmt from the model driven app. However it would be nice to access the folder structure of the team site from the model driven app, not the auto created folder when syncing sharepoint to model driven apps natively.

Hi Matthew, thank you for all your blogs, I really appreciate them! I’m curious as to what’s your strategy to have a more “user-friendly” folder name in SharePoint… I usually use Power Automate to create the folder with a unique name (but “readable”) and the correspondent Document Locations record.

My trigger is usually the moment the Dataverse record is created, so that users without access to the Power App (or those accessing directly the SharePoint site) can load files from the very start, but I’m keen on learning your thoughts!

Another topic is accessing these files from a Canvas… but that’s for another post!

Cheers mate 🙂

Hi Matthew, great post, very helpful (like the others for that matter)

I have been thinking about these issues for a long time and I have two questions:

1) Some documents need to be viewed only by some (e.g. payroll) while others can be viewed by all. is it possible to do this with Sharepoint / Model-Driven App integration?

2) Can I also use the integrated collection in a Canvas app as well as in a Model Driven app?

Always thank you for your work

Translated with DeepL.com (free version)

Marco,

1. Documents with different permissions seems like a difficult requirement since SharePoint and Dataverse have different security models.

2. Yes, I have used the integrated collection in a canvas app. You could do it directly. Or what I did is create a flow to retrieve documents using the service account and also open as the service account. This allows the user to access docs without granting permission to SharePoint.

Hi Matthew,

2. Don’t you have more information on how to use Power Automate to read documents from SharePoint document libraries using the service account and response them to the canvas app?

Thanks,

Albi

Hey Matt,

Thanks for a great article, as usual!

I was wondering if you have any advice to do multiple files in a single upload (sorry if this is something you have already covered).

Thanks,

Alice

Alice,

That would have to be built custom with a drag and drop PCF control and your own flow.

https://pcf.gallery/drag-and-drop-file-uploader/

Or you could educate the user to click “Open Location” on the menu bar of the SharePoint library subgrid and that will open the corresponding SharePoint page. Then the user can knock themselves out with multiple uploads, folder creation, adding metadata to the SharePoint library, etc., in the SharePoint page.

Great post, thanks!

I’ve got an issue with the two views that appear on the subgrid when linked to the “Documents (Regarding)” table, as follows:

The “Document Associated Grid” – DAG for short – does not appear in the Default view property dropdown list of the subgrid. Only the “All SharePoint Document” view is listed in the dropdown – see attached image. So I can’t set the “DAG” as the default view.

I want the “DAG” view to be the default view in my custom “Documents” tab (like it is in the “Related Documents” tab called “Documents”) because the DAG view shows the folders and subfolders of the SharePoint document location with navigation up and down via breadcrumb trail, whereas the “All SharePoint Document” view does not.

How can I set the default view of the subgrid to the DAG?

Fantastic solution. One question – is there a way to store documents in a specific folder in the document library or does it only store the way you showed in this blog?

Salil,

The base folder will always be the table name and I would not recommend changing it (example: Accounts table). But you can build a Power Automate flow to retitle the subfolder’s record name. I would make the trigger “When A New Record Is Added” to the Document Locations table.

Salil,

No, you cannot come up with your own custom structure. The best you can do is use a flow to rename folders

There are third party tools that let you configure how to structure the documents in SharePoint and you can also use Power Automate to create your own folders and Document Locations the way you like. Of course doing custom stuff like that comes with extra opportunities for bugs and future rework 😉

Hi ,

Is there a way to see the version history and the share option within the grid itself when select the document we can see the version history and the share option. when we add the document grid the “”folder” option is not there , can we add in the grid itself, rather then select documents option under the related tab. Kindly help in these that we would great help.

Hi Matthew, thanks for this demo. Unfortunately, my version of Dataverse / Model Driven App does not support Advanced Settings, so no Document Managment option. Do you know of a work around or do I need my organization to upgrade. We currently are licensed for Power Apps / Model Driven Apps but I don’t know what upgrades we need to achieve the SharePoint integration.

Thanks!

David,

Open a support ticket with Microsoft. It’s likely a bug.

I have a use case where we are using SharePoint integration in a model-driven app for document storage. One of the entities using documents are subcomponents where multiple subcomponents that are same model and version could have the same manufacturing guide, specs sheet, etc.

Is there a way, using SharePoint integration, to share a single document for multiple subcomponents and avoid duplicating the document and storing multiple copies for each item?

Great post and thank you!

I’m using document integration for multiple model driven apps on one environment.All apps have their own DEV environment. “IsDocumentManagementEnabled” seems to be the table metadata that defines whether this out of the box SharePoint document integration is active. It all went fine until with our latest solution which contains a shared table that has document integration enabled from a previous app but doesn’t need it in the new app. The tables metadata is not in this new solution (metadata of shared tables are only included in one global solution which also has it’s separate DEV environment), yet the shared table’s document integration gets turned off when I import the new solution. I have other solutions that also contain that same table without the metadata and they don’t interfere with the document integration.

I forgot to attach my screenshot. Here it is.

Hi Matthew, first of all I’d like to express my gratitude for your such detailed show and tell article. It’s very helpful!! I followed your instruction, and everything went well except the last step of showing all associated files in the Documents tab. It pops out message saying, “Collaborate and share files easily-ask your admin to enable SharePoint.” Would you please advise me on this part? I have very limited knowledge of SharePoint. Much appreciated your help!!!

Sorry it’s me again, please ignore my last comments. I found out why. Thank you!

Hi Matthew, sorry to bother you again. In this documents table, is there a way to edit prosperities? When I select a file, go to the edit property, it only has two options: Name and Title. In fact, I created a column called document type and I’d like to have the document type shown in edit property dialog. Would you please share some light on this? Much appreciated your help.

Thank you, Dan for your excellent and clear description, but I have a question: usually I develop all my Apps in a developer environment and then I move them in a production environment by a managed solution. I have been using the same procedure you describe since man years, without any problem, but, since a few months I noticed that this procedure creates an “active” layer for each table where a SharePoint Doc Library is created. This is very annoying because it prevents future customization to be imported into those tables. What do you recommend solving this problem?