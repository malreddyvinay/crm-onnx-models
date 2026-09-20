## Q. How to show and hide tabs using Javascript in Dynamics 365?

Follow the below video to see the implementation-

**Introduction:**

Dynamics 365 is a robust and versatile customer relationship management (CRM) platform developed by Microsoft. One of the key strengths of Dynamics 365 is its flexibility in customization. In this blog post, we will explore a powerful customization technique using JavaScript to show and hide tabs within Dynamics 365. This technique allows you to tailor the user interface to display relevant information based on user actions or specific conditions, enhancing the overall user experience and productivity.

**Prerequisites:**

Before diving into the implementation, ensure you have the necessary access and permissions to customize forms within Dynamics 365. Additionally, a basic understanding of JavaScript and Dynamics 365 customization concepts will be beneficial.

**Step 1: Identify the Target Form**

The first step is to identify the form on which you want to implement the show/hide tabs functionality. Navigate to the Dynamics 365 customization area and open the form customization editor for the desired entity.

**Step 2: Create a Web Resource**

To encapsulate the JavaScript code, we need to create a web resource within Dynamics 365. This resource will store the JavaScript code and can be referenced within the form customization. Create a new web resource and specify the appropriate name and type (JavaScript).

**Step 3: Add JavaScript Code**

Inside the web resource, add the JavaScript code responsible for showing and hiding tabs. The code will typically use the Xrm.Page object model to interact with the form and its components. Here's an example code snippet to get you started:

**// Function to show or hide tabs based on the visit type field**

*function showHideTabsBasedOnVisitType(executionContext) {
var formContext = executionContext.getFormContext();
// Get the visit type field value
var visitType = formContext.getAttribute("cbt_visittype").getValue();
// Get the tab controls
var Tab1 = formContext.ui.tabs.get("tab_tab1name");
var Tab2 = formContext.ui.tabs.get("tab_tab2name");
var Tab3 = formContext.ui.tabs.get("tab_tab3name");
var Tab4 = formContext.ui.tabs.get("tab_tab4name");
// Show or hide tabs based on the visit type
if (visitType == 1) { //Instructor Standards Checks
Tab1.setVisible(true);
Tab2.setVisible(false);
Tab3.setVisible(false);
Tab4.setVisible(false);
} else if (visitType == 2) { //ComplianceChecks
Tab1.setVisible(false);
Tab2.setVisible(true);
Tab3.setVisible(false);
Tab4.setVisible(false);
} else if (visitType == 3) { //Educational PR-Visits
Tab1.setVisible(false);
Tab2.setVisible(false);
Tab3.setVisible(true);
Tab4.setVisible(false);
} else if (visitType == 4) { //Site Inspections
Tab1.setVisible(false);
Tab2.setVisible(false);
Tab3.setVisible(false);
Tab4.setVisible(true);
} else {
// If the visit type is not set or doesn't match any condition, hide all tabs
Tab1.setVisible(false);
Tab2.setVisible(false);
Tab3.setVisible(false);
Tab4.setVisible(false);
}
}*

var formContext = executionContext.getFormContext();

// Get the visit type field value

var visitType = formContext.getAttribute("cbt_visittype").getValue();

// Get the tab controls

var Tab1 = formContext.ui.tabs.get("tab_tab1name");

var Tab2 = formContext.ui.tabs.get("tab_tab2name");

var Tab3 = formContext.ui.tabs.get("tab_tab3name");

var Tab4 = formContext.ui.tabs.get("tab_tab4name");

// Show or hide tabs based on the visit type

if (visitType == 1) { //Instructor Standards Checks

Tab1.setVisible(true);

Tab2.setVisible(false);

Tab3.setVisible(false);

Tab4.setVisible(false);

} else if (visitType == 2) { //ComplianceChecks

Tab1.setVisible(false);

Tab2.setVisible(true);

Tab3.setVisible(false);

Tab4.setVisible(false);

} else if (visitType == 3) { //Educational PR-Visits

Tab1.setVisible(false);

Tab2.setVisible(false);

Tab3.setVisible(true);

Tab4.setVisible(false);

} else if (visitType == 4) { //Site Inspections

Tab1.setVisible(false);

Tab2.setVisible(false);

Tab3.setVisible(false);

Tab4.setVisible(true);

} else {

// If the visit type is not set or doesn't match any condition, hide all tabs

Tab1.setVisible(false);

Tab2.setVisible(false);

Tab3.setVisible(false);

Tab4.setVisible(false);

}

}

The above code assumes that you want to show or hide a tab based on the value of a specific field on the form. Modify the tabName variable to match the name of the target tab, and update the condition variable to reference the field name and its desired value.

**Step 4: Add the JavaScript Code to the Form**

After saving the web resource, go back to the form customization editor. Add a new form event handler to invoke the showHideTabs function whenever the form loads or a specific event occurs (e.g., field value change). Specify the appropriate event and add a reference to the web resource containing the JavaScript code.

**Step 5: Publish and Test**

Save the changes to the form customization, publish the form, and navigate to the entity's record to test the show/hide tabs functionality. Verify that the tabs are displayed or hidden based on the specified condition and user interactions.

**Conclusion:**

Customizing Dynamics 365 forms using JavaScript provides immense power and flexibility to tailor the user experience to specific business requirements. By leveraging the show/hide tabs technique outlined in this blog post, you can enhance the usability and relevance of your Dynamics 365 forms, ultimately improving user productivity and satisfaction. Experiment with this technique, explore other customization possibilities, and unlock the full potential of Dynamics 365 to meet your organization's unique needs.

## No comments:

## Post a Comment