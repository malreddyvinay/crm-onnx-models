# How To Set An Email Category In Power Automate

Power Automate can be used to set an email category. A category is an feature that allows you to tag, label and group messages. Emails also become easier to spot because a badge is displayed with the category name. There is no dedicated action for setting a category but it’s possible to do with the Outlook Send An HTTP action – which by the way does not require any premium licensing.

### 



**Introduction: The “Top Customer” Sales Email Automation**

Salespeople at a manufacturing company talk with their customers over email.  When a new email is received from a “top customer” Power Automate applies a category to the email to make it easier for the salesperson to identify.


For example, “Top Customer” appears as badge for this new email from [email protected].

### 



**Update An Email Category Name In Outlook**

Email categories are maintained in Outlook 365. There are several color coded preset categories by default. We want to update an existing category to read “Top Customer” instead.

Go to Outlook.com and right-click on any email in the inbox. Choose *Categorize*.  Then select *Manage Categories*.


Change the name of one of the existing categories to “Top Customer” and close the menu.

### 



**Configure The “When A New Email Arrives” Trigger Settings**

Open Power Automate and create a new automated flow using the *Office 365 Outlook – When A New Email Arrives (V3*) trigger. Choose the *Folder* named Inbox.  Select an an account that can send an email to the inbox in the *From* field.  This account will serve as a “Top Customer.”


Go to the trigger’s Settings and enable *Split On*.  This tells Power Automate to evaluate each email individually as it arrives in the inbox.

### 



**Set An Email Category Using The Microsoft Graph API**


**Set An Email Category Using The Microsoft Graph API**
We must use the Microsoft Graph API to set an email’s category since it does not appear as a standard action in Power Automate.  Add an *Office 365 Outlook – Send An HTTP Request* action to the flow and select the PATCH method.


Use the following *URI* to update the message object.

`https://graph.microsoft.com/v1.0/me/mailFolders/Inbox/messages/@{triggerOutputs()?['body/id']}`Code language: JavaScript (javascript)

Supply this JSON to the *Body* of the action.

```
{
"categories": ["Top Customer"]
}
```
Code language: JSON / JSON with Comments (json)

Write this code in the *Content-Type* field.

`application/json`
### 



**Run The Flow To Set The Email Category**

Now that our very simple flow is completed let’s try it out.  Save the Power Automate flow in the editor and start a manual test.  Then send a new email to the target inbox using the account we chose in the trigger’s *From* field.


The flow will completes successfully.


And a “Top Customer” badge shows within the email to display its’ category.

### **Did You Enjoy This Article?**   😺

Subscribe to get new Copilot Studio articles sent to your inbox each week for FREE

### 



**Questions?**

If you have any questions or feedback about **How To Set An Email Category In Power Automate** please leave a message in the comments section below.  You can post using your email address and are not required to create an account to join the discussion.

Thank you for your great articles Matthew.

Have you found a way to read the categories from an email?

Is there a way to have Power Automate create a category when emails are sent out and then put it on those messages?

Damien,

Yes, just change the trigger form “When an email is sent” to “When an email is received.”

By chance, is there anyway to apply colour coding within the flow for the category badge? – so that if multiple categories are assigned, certain categories are different colours.

Jay,

I would create the category and set their colors in advance using MS Outlook.

Can’t make It work… I Always get grey color tags, and also they are not saved in Outlook.

Anyone here found a way to do that?

can we have chance to remove category from email

Excellent – and now the other way around 🙂 When I manually set a label on an email, I want a flow to ask me to enter a date, set a reminder and set a follow up flag, so it appears in my todo.

I wonder how the trigger “when a label soandso, then..” is set.

I second this request, How to set a trigger on a mailbox to do something with an existing mail after assigning a category to it

Thank you for your great blog, this is really helpful. I’m looking for the flow

Hi! I have just tried this method and I received an error message “The OData request is not supported.”. Do you have any idea what could be wrong? 🙁

Update: no worries, found the problem!

Marti,

What was the issue you had? Others could learn from it.

I was not attentive enough, didn’t see that I chose the wrong method!

Is there a way to read those categories and export them (from, to, body, category) to a SharePoint list using power automate

I am curious about this too – I want to do exactly this 🙂

Hi Matthew – How can i do the same for a shared mailbox instead of my personal mailbox?

Thank you for all of your articles!

Nevermind – I was able to find it out. I have attached a picture to showcase how it was configured.

That’s great, thank you for posting.

Do you also know a way to change color to the category? I always get a grey category, no matter the category.

Another point, i can’t see the categories used in “category” menu (in outlook web, go to settings >>> general >>> Categories). I see only “Category <color>”.

Thanks to this i found my solution, thank you.

Trying to do exactly this but I get error message “The request must be chunked or have a content length”. Do you have any suggestion on how to handle this? I tried adding Content-Length in the body. Thank you!

Thank you, how you would direct the folder to look a subfolder instead of the inbox? I have tried ‘Inbox\SUBFOLDER’ but this gives me an error?

How to get category from outlook using power automate. When new email received. Check category, once category updated capture category to excel

Hi, Matthew! Can the flow be modified to add a category to any existing category on the email–and not replace the existing category?

Never mind. I have a flow that categorizes each email with the sender’s domain, and at first I thought each email in a conversation was overwriting the category. It’s not doing that–it’s adding a category with each new email.

How to setup flow

Is there a way to control the color of each category? I can’t find a way to do that, even if categories are already there. All the categories are applied to mail, but always with grey color.

Hi Matthew ,

I tried to apply your way using GPT to generate dynamic categories but always getting HTTP request now working

I added all the details in Microsoft Forums for Power Automate

https://community.powerplatform.com/forums/thread/details/?threadid=ce9d5cb6-337f-ef11-ac21-6045bdd74f2e

Excellent, thanks!

Is any authentication required?

Plaman,

Authentication is handled without any additional coding by Power Automate.

but need an authentication token for the shared mail boxes right?

Sasitha,

No authentication token is needed since you you are accessing it through a connection with an account which it is shared to.

can we remove category from email

This worked perfectly for me, and assigned the colour I had set in Outlook too.

Good post; thanks for helping

How could this be modified to work for calendar events? Ex. With the trigger being “When a new event is created” in an attempt to auto-assign a category for any event with the title “Focus Time”