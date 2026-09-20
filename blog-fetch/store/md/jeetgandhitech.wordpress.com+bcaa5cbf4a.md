### **What is a Custom Connector?**

A Custom Connector enables you to connect Power Automate (or Power Apps/Logic Apps) to any REST API using a definition (such as OpenAPI/Swagger), allowing you to utilize that API as if it were a native connector.

**Pre-requisites:**

- A Power Platform environment (Power Automate or Power Apps).
- An OpenAPI (Swagger) definition file (either .json or .yaml).
- API Key, OAuth 2.0, or any other required authentication info (if applicable).

#### **Step 1: Go to Power Platform Makers portal**

- Visit: https://make.powerapps.com/
- Sign in with your work/school account.

#### **Step 2: Navigate to Custom Connectors**

- From the left menu, go to “Custom connectors” as shown below

- Click on “+ New custom connector”
- Choose “Import an OpenAPI file”

#### **Step 3: Import Your OpenAPI File**

- Name your connector
- Click “Import” and select your .json or .yaml OpenAPI/Swagger file.
- Click Continue

#### **Step 4: General Information**

- You’ll see a form with:
  - **Scheme** : HTTPS (default)
  - **Host** : Domain from the OpenAPI file
  - **Base URL** : From the definition
- You can edit icons, description, etc.
- Click “Security” tab when done.

#### **Step 5: Configure Authentication (Security Tab)**

- Choose the authentication type:
  - No authentication
  - Basic authentication
  - API Key
  - OAuth 2.0 (Azure AD, generic OAuth)
- Provide the required details based on type.
- Click “Definition” tab.

#### **Step 6: Review Actions and Triggers (Definition Tab)**

- The OpenAPI file will auto-populate the actions (operations).
- You can:
  - Review request and response parameters
  - Add summaries/descriptions for clarity
  - Customize visibility of parameters

#### **Step 7: Test the Connector**

- Click on “Test” tab
  - Save and click “Create connector”
  - Authenticate (if required)
- Run the test for any of the listed actions to ensure it works.

#### **Step 8: Use the Connector in Power Automate**/PowerApps

### **Tips:**

- Always test with real inputs to validate schema and outputs.
- Update the OpenAPI file to add new endpoints and re-import or edit directly.
- If using OAuth, you might need to register an app in Azure AD.

**Please let me know in the comments if you need any further details about this topic. You can also ask about any other way of creating Custom Connectors in Power Platform.**

## Leave a comment