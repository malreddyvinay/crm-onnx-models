A Custom API in Dynamics 365 is a server-side operation that lets you define and execute custom business logic. It acts like a custom message or action that can be used in workflows, plugins, Power Automate, and external applications.

### **Why Use Custom API?**

- Execute complex operations in one API call.
- Reusable in multiple processes.
- Supports input and output parameters.
- More flexible and maintainable than Custom Actions.

### **Key Components of Custom API**

1. Custom API – The definition of the API itself.
2. Custom API Request Parameter – Input parameters.
3. Custom API Response Property – Output parameters.
4. Plugin or Custom Code – The business logic associated with the API.
5. Invocation – Using the Custom API in Power Automate, JavaScript, C#, or external applications.

### **Creating a Custom API in Dynamics 365**

#### Step 1: Create the Custom API

- Go to Power Apps → Solutions → Select your solution.
- Click on New → Other → Custom API.
  - **Name** : new_CalculateDiscount → (Unique name for your API)
  - **Display Name** : Calculate Discount
  - **Binding Type** :
    - Global: Available without associating with a specific entity.
    - Entity: Requires an entity record.
    - EntityCollection: Works with multiple records.
  - **Bound Entity Logical Name** : (Select the entity if binding is required)
  - **Allowed Custom Processing Step Type** : None or Sync/Async Plugin Execution.
  - **Execute Privilege Name** : (Optional) Security privilege required.
  - **Is Function** : No (Function if it’s query-based; otherwise, it’s an Action)
  - **Is Private** : No (If you want it available to Power Automate or external apps)
- Save and publish the Custom API.

#### Step 2: Define Request Parameters

- In the Solution Explorer, go to your Custom API.
- Click + New → Custom API Request Parameter.
  - **Name** : Amount
  - **Display Name** : Purchase Amount
  - **Type** : Decimal
  - **Is Optional** : No
  - **Unique Name** : new_Amount

👉 Add multiple parameters if needed (e.g., DiscountRate).

#### Step 3: Define Response Properties

- Go to your Custom API.
- Click + New → Custom API Response Property.
  - **Name** : DiscountedPrice
  - **Display Name** : Final Price after Discount
  - **Type** : Decimal
  - **Unique Name** : new_DiscountedPrice
- Save and publish the changes.

#### Step 4: Add Plugin to Implement Business Logic

- Open Visual Studio and create a Class Library Project.
- Add NuGet Packages:
  - Microsoft.CrmSdk.CoreAssemblies
  - Microsoft.CrmSdk.Plugin
- Add a new class CalculateDiscountPlugin.cs.

```
using Microsoft.Xrm.Sdk;
using System;
public class CalculateDiscountPlugin : IPlugin
{
    public void Execute(IServiceProvider serviceProvider)
    {
        IPluginExecutionContext context = (IPluginExecutionContext)serviceProvider.GetService(typeof(IPluginExecutionContext));
        if (context.MessageName != "new_CalculateDiscount")
            return;
        decimal amount = (decimal)context.InputParameters["new_Amount"];
        decimal discountRate = 0.1m; // 10% discount
        decimal discountedPrice = amount - (amount * discountRate);
        context.OutputParameters["new_DiscountedPrice"] = discountedPrice;
    }
}
```
- Build the Plugin, and sign it with a strong name.

#### Step 5: Register the Plugin

- Use Plugin Registration Tool:
  - Click Register New Assembly → Select your .dll.
  - Click Register New Step:
    - **Message** : new_CalculateDiscount
    - **Stage** : Post-operation
    - **Mode** : Synchronous
- Click Register.

### **Testing the Custom API**

- **Via Postman**  - Go to Power Apps → Settings → Developer Resources.
  - Get the Web API URL and Access Token.
  - Use the following request in Postman:
    - URL: https://<your-org>.api.crm.dynamics.com/api/data/v9.2/new_CalculateDiscount
    - Method: POST
    - Headers:
      - Authorization: Bearer <access_token>
      - Content-Type: application/json
    - Body:

✅ Expected Response:

```
{
    "new_DiscountedPrice": 900
}
```
- **Using Custom API in Power Automate**  - Go to Power Automate → Create Flow.
  - Select “When a record is created” (Dataverse Trigger).
  - Add “Perform an unbound action”.
  - Select your Custom API: new_CalculateDiscount.
  - Add parameters and map them to the flow variables.
  - Use the output parameter (new_DiscountedPrice) in further steps.

### **Use Cases of Custom API in D365**

- Bulk operations: Execute complex operations in bulk.
- Custom calculations: Discounts, taxes, or complex financial logic.
- Integration: Trigger external APIs with pre-processed data.
- Automation: Used in Power Automate and Plugins to execute reusable logic.

### **Key Differences: Custom API vs. Custom Actions**

| **Feature** | **Custom API** | **Custom Actions** | 
| Execution | Lightweight and faster | Slightly slower | 
| Reuse | Easily reusable | Reusable but less flexible | 
| Complexity | Supports Multiple parameters | Supports fewer parameters | 
| Usage | Better for external integration | Used more internally in D365 | 
| Return Types | Supports multiple output values | Limited return types | 

### **Best Practices**

- Use Custom API for reusable logic rather than Custom Actions.
- Implement error handling in the plugin code.
- Use privileges to control access.
- Test the API thoroughly with Postman and Power Automate.

### **Conclusion**

Custom APIs in Dynamics 365 offer a powerful and flexible way to define and execute server-side operations. With reusable business logic, they enhance efficiency and streamline integrations.

## Leave a comment