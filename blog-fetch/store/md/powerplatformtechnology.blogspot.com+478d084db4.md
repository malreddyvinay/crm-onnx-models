### Syncing Power Automate Approval Status Across Teams, Outlook, and Apps

## Introduction

Power Automate provides robust approval workflows that integrate seamlessly with Microsoft Teams, Outlook, and custom applications. However, synchronizing approval statuses across these platforms remains a challenge. This blog will discuss a practical solution to ensure that approvals made from one platform reflect across all others without relying on Microsoft Graph API (which is currently in preview) or complex Azure AD app registrations.

## The Challenge

A user receives approval requests via:

- **Microsoft Teams**
- **Outlook**
- **A direct link to the app**

If a user approves the request from the app, it should also reflect as approved in Teams and Outlook. However, Power Automate lacks a built-in feature to achieve this easily. Microsoft Graph API can perform approval actions but remains in preview mode, making it unsuitable for production. Additionally, registering an app in Azure AD increases complexity and maintenance efforts.

## The Solution

To overcome this challenge, I designed a simple yet effective workaround using Power Automate and HTTP actions. Here's how it works:

### **Step 1: Create an Approval Request**

1. Use the **Create an approval** action in Power Automate to generate an approval request.
2. Store the approval ID along with the related record in a custom column.

### **Step 2: Wait for User Action**

1. Add a **Wait for approval** action in Power Automate to listen for user responses.
2. If the user approves via Teams or Outlook, the approval status updates automatically.

### **Step 3: Handling Direct App Approvals**

1. When a user approves the request directly from the app, trigger another Power Automate flow.
2. This secondary flow, running in the user’s context, executes an approval request update.
3. Use the **Invoke HTTP Action** (with pre-authorized Entra ID) to update the approval status via API directly within the flow.
4. This ensures that the approval status syncs across all platforms in real-time.

### **Step 4: Supporting Reassignments**

If the approval request is reassigned to another user, the flow still functions seamlessly. The reassigned user receives the updated approval request, and the sync process continues as expected.

## **Key Benefits**

- **No dependency on Graph API** (avoiding preview-mode restrictions)
- **No need for complex Azure AD app registrations**
- **Real-time synchronization across Teams, Outlook, and custom apps**
- **Works even when approvals are reassigned to another user**


**Create Approval Flow**

## 
**Approve Approval Instant Flow**

Approve Approval Instant Flow

**Action Name :**Invoke an HTTP request (pre Authorized)


**Base Resource URL**


**Azure AD Resource URI (Microsoft Entra ID Resource URI (Application ID URI)) :**

**Method :** 

POST


**Request URL:**
https://api.flow.microsoft.com/providers/Microsoft.ProcessSimple/environments/@{workflow()?['tags']?['environmentName']}/approvals/c88eabf4-b346-418b-9b30-2a9767e1ec26/approvalResponses?api-version=2016-11-01
**Headers:**
Content-Type:application/json
**Body of the request:**
{properties: {response: "Approve", comments: "Request Approved"}}
OR
{properties: {response: "Reject", comments: "Request Rejected"}}


## **Conclusion**

This approach provides a simple yet powerful method to synchronize approval requests across multiple platforms in Power Automate. By leveraging HTTP actions with Entra ID and structuring flows effectively, users can experience seamless approval management without additional overhead.

Would you try this solution in your Power Automate workflows? Let me know your thoughts!

## Comments

## Post a Comment