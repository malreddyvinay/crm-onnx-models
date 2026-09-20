# Custom API/Web service in D365 using X++

Dynamic D365 AX Developer

Hello Reader,

I hope you're familiar with what an API is and how it functions. If not, here's a brief overview:

An **API (Application Programming Interface)** allows different software applications to communicate with each other. It defines the methods and data formats that applications can use to request and exchange information.

**When Should You Create a Custom API in Dynamics 365 F&O?**

You should consider creating a custom API in Dynamics 365 F&O when you need to:

- **Process External Data:** If your organization needs to process data received from external systems or applications, a custom API can facilitate this integration. For example, if a third-party application sends order data to your system, a custom API can handle the incoming data and process it accordingly.
- **Expose Business Logic:** When you want to expose specific business logic or operations to external applications, a custom API can make this possible. For instance, if you have a custom business process that needs to be accessed by other systems, a custom API can provide the necessary interface.
- **Integrate with External Systems:** If your organization requires integration with external systems such as CRM, ERP, or third-party applications, a custom API can serve as the bridge between your Dynamics 365 F&O system and these external systems.

## **Creating a Custom API in Dynamics 365 F&O:**

To create a custom API in Dynamics 365 F&O, follow these steps:

1. **Define the Service Contract:** Create a Data Contract class in X++ that defines the data structure for the API.
2. **Implement the Service Operations:** Develop a Service class with methods that contain the business logic to be exposed by the API.
3. **Create the Service and Service Group:** In the Application Object Tree (AOT), create a Service and a Service Group to group related services together.
4. **Deploy the Service:** Deploy the custom service to make it available for consumption.
5. **Consume the Service:** External applications can now call the API using standard protocols like REST.

### ✅ Step 1: Define the **Service Contract** (Data Contract Class)

```
[DataContractAttribute]
public class CustomerDataContract
{
    str name;
    str email;
    str phone;
    str city;
    [DataMemberAttribute("Name")]
    public str parmName(str _name = name)
    {
        name = _name;
        return name;
    }
    [DataMemberAttribute("Email")]
    public str parmEmail(str _email = email)
    {
        email = _email;
        return email;
    }
    [DataMemberAttribute("Phone")]
    public str parmPhone(str _phone = phone)
    {
        phone = _phone;
        return phone;
    }
    [DataMemberAttribute("City")]
    public str parmCity(str _city = city)
    {
        city = _city;
        return city;
    }
}
```
Create a new class called `CustomerDataContract`. This class defines the structure of the data that will be sent to the API.

### ✅ Step 2: Implement the **Service Operation** (Service Class)

This is where the logic for handling the request is written. The service will accept the contract data and insert it into a **custom table** called `CustomCustomerTable`.

```
public class CustomerService
{
    public void createCustomerRecord(CustomerDataContract _contract)
    {
        CustomCustomerTable customerTable;
        ttsBegin;
        customerTable.Name  = _contract.parmName();
        customerTable.Email = _contract.parmEmail();
        customerTable.Phone = _contract.parmPhone();
        customerTable.City  = _contract.parmCity();
        customerTable.insert();
        ttsCommit;
    }
}
```
## ✅ Step 3: Create the Service and Service Group

This step involves registering your service logic and exposing it through a service group, which can then be consumed externally (e.g., via REST).

### 🔹 1. **Create the Service**

In Visual Studio (with Dynamics 365 F&O development environment):

1. **Right-click** on your project >**Add > New Item**
2. Choose **Service** , name it`CustomerService`
3. In the Service properties: 
  - **Class** : Point it to your`CustomerService` class created in Step 2
  - **Service Name** :`CustomerService`
  - **Label/Description** (optional): Add a meaningful description
4. Create a new service operation and configure its properties as shown in the screenshot.

### 🔹 2. **Create the Service Group**

This is what makes your service available for external access.

1. **Right-click** on your project >**Add > New Item**
2. Select **Service Group** , name it`CustomerServiceGroup`
3. Select **New Service** .
4. In the **Properties** window, set the following values:
  - **Name** →`CustomerService`
  - **Service** →`CustomerService`*(this should point to the service object you created earlier)*

## ✅ Step 4: Deploy the Project

Once you’ve created the **Data Contract**, **Service Class**, **Service**, and **Service Group**, the final step is to **deploy** the service so it can be accessed externally.

## ✅ Step 5: Test the Custom API

Once the service is deployed, it's time to **test the API** to make sure it works as expected and can receive and process data from external systems.

### **The real challenge starts from here.**

**Prerequisites for Connecting to Dynamics 365 via API.(service we created)**

Before you can connect to Dynamics 365 Finance and Operations through an API, you need the following information:

- **Client ID**
- **Client Secret**
- **Tenant ID**

These credentials come from an app registration in **Microsoft Azure Active Directory**.

🔐 **If you don’t have these details**, you’ll need to contact your **system administrator** or **client** and request them to:


1. **Register an application** in the Azure Portal.
2. Provide you with the **Client ID** ,**Client Secret** , and**Tenant ID** after the app is registered.

These values are used for **authentication** when calling APIs securely via **OAuth 2.0**.

## How to Get and Use a Bearer Token in Postman for Dynamics 365 F&O

### 🔹 Step 1: Set Up a Token Request in Postman

1. **Open Postman**
2. Create a **new request tab**
3. Set method to `GET`
4. In the **URL field** , enter:`https://login.microsoftonline.com/<your-tenant-id>/oauth2/v2.0/token`

### 🔹 Step 2: Go to the **Body** Tab

1. Select `x-www-form-urlencoded`
2. Add the following key-value pairs:

| Key | Value | 
| `grant_type` | `client_credentials` | 
| `client_id` | *(Your Azure app's client ID)* | 
| `client_secret` | *(Your Azure app's client secret)* | 
| `resource` | `https://<your-env>.``cloudax.dynamics.com` (your D365 F&O base URL) | 

In header parameter, add key as `Host` and value as`login.microsoftonline.com`

Click send and you will get the token:

Now send the request to create the record in F&O:

#### **1. Set up the Endpoint URL in Postman**

- **Method** :`POST`
- **URL** :`https://<your-f&o-url>/api/services/CustomerServiceGroup/CustomerService/createCustomerRecord`

**2. Set the Headers**

In the **Headers** tab of Postman, add the following headers:

- **Authorization** : Auth Type set to`Bearer Token` and paste the`access_token` value in Token

#### **3. Send the Request and “BOOM”**

Once everything is set up, click the **Send** button in Postman.

## **Note: You need to set up the Client ID in the Microsoft Entra ID applications form in Dynamics 365 with Admin user.**

I know this is a simple example I’ve provided, but there are many other ways to handle requests with multiple JSON objects and different values being returned as multiple JSON responses.