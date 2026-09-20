In this blog post, we will learn a new code snippet of JavaScript that we are using to implement a requirement in a Model Driven App. The feature is called “**setDefaultView()”**, and it allows us to dynamically change the default view of a lookup field.

**Requirement**:

Filter the lookup values of the contact entity on the account entity based on the selected option in the ownership column. The ownership column is an option set type column with four options:

- Public
- Private
- Subsidiary
- Others

We want to show only the contacts that belong to the same ownership type as the account in the lookup field.

**Implementation:**

To achieve this, we are using the **setDefaultView()** method of the lookup control in JavaScript. This method takes a view ID as a parameter and sets it as the default view for the lookup field. We can use this method in the OnChange event handler of the ownership field to dynamically change the default view of the contact lookup field based on the selected option.

- We have an option set column of “**Ownership** ”.
- Based on the options, we have created views.
- And we have a lookup column of contact entity.
- Also, we have an option set column of ownership on Account entity .

- If value in ownership is selected as “**Public** ”, only public view records will be suggested in lookup.

```
//Option set Values of "Ownership" field.
const Ownership = {
	PUBLIC:1,
	PRIVATE:2,
	SUBSIDIARY:3,
	OTHER:4,
 
};
 
//To set the Custom View on Lookup Field.
function SetDefaultViewOnContact(executionContext)
{
   var formContext = executionContext.getFormContext();
   if (formContext.getAttribute("ownershipcode") != null  && formContext.getAttribute("ownershipcode").getValue() != null)
   {
	   //To retrive the "Ownership" of current record.
	   var OwnershipAcc = formContext.getAttribute("ownershipcode").getValue();
        switch(OwnershipAcc) 
	    {
			case Ownership.PUBLIC:
			formContext.getControl("primarycontactid").setDefaultView("{13E3DEA0-09C0-EE11-9079-000D3A337001}");
			break;
			case Ownership.PRIVATE:
			formContext.getControl("primarycontactid").setDefaultView("{48AEAFA1-0BC0-EE11-9079-000D3A337001}");
			break;
			case Ownership.SUBSIDIARY:
		    formContext.getControl("primarycontactid").setDefaultView("{CB830663-17C0-EE11-9079-000D3A337001}");
			break;
			default:
            formContext.getControl("primarycontactid").setDefaultView("{608861BC-50A4-4C5F-A02C-21FE1943E2CF}");
        }
   }
}
```
This way, we can provide a better user experience and filter out irrelevant lookup values based on the context. The setDefaultView() method is a new feature of JavaScript that is available in Model Driven Apps and can be used for various scenarios where we need to dynamically change.

**Output:**

Hope it helps!

Power 365ing as usual!

Any requirements, implementation or consulting work in Power Platform or Dynamics 365 – end user, Microsoft partner or an individual?

Problem Area – Technical, Functional, Training, Development or consulting?

Me and my team are here to assist, please fill the following form for your business needs: Click here