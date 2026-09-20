### How to Embed Audit History on a Form in Model-Driven App

    This post will explain how you can embed an audit history on the form of a
    table using an iFrame control and JavaScript.
  

  
    If you do not want the users to click multiple times on 

**Related**tab and then**, you can show it on the form directly or under a separate tab by adding an iFrame control and set the URL of the iFrame using JavaScript.***Audit History*
**🛈 Note**

Please be aware that the current Audit History is one of the certain legacy UI which is enabled as part of hybrid experience in Unified Interface. When Microsoft implement the Audit History in full Unified Interface experience, you will have to re-implement this functionality.

To add an iFrame to the form, select the 

**External website**component in the form designer and set the site URL with a dummy URL. Set the name of the iFrame control as well which will be used in the JavaScript below. (for sample code, "IFRAME_audit" is used as the name of an iFrame)
Embedding the Audit History in the IFrame will require JavaScript to
      populate the entity ID and object type code parameters. WebAPI request
      will be required to get Object Type Code and the sample JavaScript function below can be called from the
    Form OnLoad event or TabStateChange event (if an iFrame is placed on a different tab).

```
 this.formOnLoad = function (executionContext)  
 {  
   setAuditIframeURL(executionContext);  
 }
```
```
 this.setAuditIframeURL = function (executionContext)  
 {  
      let formContext = executionContext.getFormContext();  
      Xrm.Utility.getEntityMetadata(formContext.data.entity.getEntityName()).then(  
      function success(entityMetadata)  
      {  
           if (entityMetadata && entityMetadata.ObjectTypeCode)  
           {  
                let objectTypeCode = entityMetadata.ObjectTypeCode;  
                let auditIFrameUrl = location.protocol + "//" + location.hostname + "/userdefined/areas.aspx?oId=" + formContext.data.entity.getId().replace("{", "").replace("}", "") + "&oType=" + objectTypeCode + "&inlineEdit=1&navItemName=Audit History&pagemode=iframe&rof=true&security=852023&tabSet=areaAudit&theme=Outlook15White";  
                formContext.getControl("IFRAME_audit").setSrc(auditIFrameUrl);  
           }  
      },  
      function (error)  
      {  
           Xrm.Navigation.openAlertDialog(  
           {  
                text: error.message  
           });  
      });  
 }  
```
For some reasons, it shows a bit differently (

**Filter**dropdown and**Delete Change History**button are not visible), so the users will not be able to filter the audit details by a specific column or delete the entire change history for that particular record from the custom audit iFrame.
One of the commenters, Sanket Kumar, also provided another script to show the OOB "Audit History" tab under by default so that the user has one less click to view Audit History without opening the 

**Related**tab.
This is the original form with just a General tab.

The following function can be called from the Form OnLoad event. The purpose of the script is focusing the Audit History tab under the Related navigation menu and focusing back to the previously focus.

```
 this.formOnLoad = function (executionContext)   
 {   
      showAuditTab(executionContext);   
 }  
```
```
 this.showAuditTab = function (executionContext)   
 {  
      let formContext = executionContext.getFormContext();   
      const navigations = formContext.ui.navigation.items;  
      const tabs = formContext.ui.tabs;  
      const focusedTab = tabs.get().find(tab => tab.getDisplayState() == 'expanded')  
      navigations.get("navAudit").setFocus(); // set focus on audit history tab  
      focusedTab.setFocus(); // set focus on the original default tab  
 }   
```
By doing so, the 

**Audit History**tab is visible by default without clicking the**Related**tab as if the user manually opened the**Audit History**tab under**Related**tab and focus back to the**General**tab.
You can also use setfocus to move audit history outside the related tab and then again setFocus on the first tab which you want to be have the default focus.

ReplyDelete
Summary

const navigations = formContext.ui.navigation.items;

const tabs = formContext.ui.tabs;

const focusedTab = tabs.get().find(tab=>tab.getDisplayState()=='expanded')

// set focus on audit history tab

navigations.get(TABS.AUDIT_HISTORY).setFocus();

// set focus on the default tab

focusedTab.setFocus();

Thanks for sharing your solution, Sanket. I have added yours in the post as well. 😊

Delete
it worked. thanks

ReplyDelete
Thanks for the feedback. I'm glad to know that there's also such a requirement in the other projects and my post solved the problem.

Delete
Hi Linn, thanks for the great post! Would this 2nd option (mentioned by Sanket) also work for the Activities Tab? I have the requirement of blending this in as a normal tab on different entities, and this would be great as the related activities tab is different (additional buttons and filters) which would not look so nicely when having to add subgrids for each activity type on a newly created tab...


ReplyDelete
Thanks for you insights!

Laura

Hi Laura


Delete
Apologies for the late reply. That script will work for the Activities tab as well. Please replace navAudit with navActivities in the script.

Hi Linn

ReplyDelete
Filter Dropdown and Delete Button only be visible if you uncheck the “Restrict cross-frame scripting, where supported.” option while adding IFRAME.

It is working for me, let me know if it is working for you as well.

Thanks,

Ankit Choubey