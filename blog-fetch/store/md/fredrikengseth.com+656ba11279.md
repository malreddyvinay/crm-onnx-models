This guide is my personal note to remember how to set up Visual Studio with KingswaySoft for ETL (Extract, Transform, Load) jobs in Dataverse and Dynamics 365. I’ll walk through the steps to install SSIS in Visual Studio Community Edition (free) and configure KingswaySoft. By following this, I’ll have a ready-to-go environment for managing Dataverse/Dynamics 365 data— and hopefully, it helps you too!

### Why SSIS?

SQL Server Integration Services (SSIS) is a powerful tool for moving, transforming, and managing data across multiple sources, making it ideal for automating workflows and handling large datasets. With **KingswaySoft’s SSIS Integration Toolkit**, it enables additional connectors, seamless integrations, bulk updates, and efficient one-time data migrations for **Dynamics 365 and Dataverse**—making it an essential tool for scalable data management.

### How to set up Visual Studio with SSIS and KingswaySoft

**Step 1:** Step 1: Download and install Visual Studio 2022 Community Edition (free) from the official website.

**Step 2:** Start the installer

**Step 3:** Say yes to “Do you want the app to make changes to this device?” that pops up if your using Windows. Screenshot not available.

**Step 4:** Continue the installation process:

When the installer starts:

**Step 5:** In the Visual Studio installer, select **Data storage and processing**, keep the rest as default > Select **Install while downloading** (default) > Then click **Install.**

Note: This will take some time to complete.

When the installation is done this window pops up.

**Step 6:** After the installation process is complete > Launch **Visual Studio**.

**Step 7:** When Visual Studio has opened > Select **Continue without code**

**Step 8:** Navigate to Extensions and search for ‘Integration.’ Select ‘SQL Server Integration Services 2022,’ then click ‘Install’ to begin the installation.

**Step 9:** This will initiate a download process in your browser, saving the file to your download folder. Once the download is complete, close Visual Studio. Then, proceed with installing the downloaded file.

**Step 10:** Install SQL Server Integration Services 2022. Open the downloaded file to start the installation process. A setup window will appear—select your preferred language to proceed.

Then click **Next** to accept the terms and privacy statements

Select the Visual Studio instance you want to install it for, Visual Studio Community 2022 we installed previously. And, click **Install.**

When the installation starts:

When the installation is finish you will see the following. Click cancel. Next, we look into how to install KingswaySoft.

**Step 9:** Open Visual Studio > Go to **Extension** > Search for **KingswaySoft** > Install **SSIS Productivity Pack** and **SSIS Integration Toolkit for Microsoft Dynamics.**

Open the installer for each of the packages and follow the step by step guide:

**Step 10:** When the installation is done > Open a **SSIS Package** > Add a **Data Flow Task** to the package > Open the **Data Flow Task** > In the left menu you will see the tools from KingswaySoft. As you can see in the next step.

**Step 11:**  After you’ve navigated to the **Data Flow Task** you see plenty of tools available for retrieving, transforming and updating data in the left side menu.

When working with SSIS, the tasks I use most frequently can be found under my Favorites in Visual Studio. To get a clearer overview, check the image below.

And, that’s the setup.

## Conclusion

By the end of this post, you should have a solid setup for using SSIS to manage and integrate data in Dynamics 365 effectively. With this setup, you’re ready to transform, migrate, and update small or large datasets efficiently.