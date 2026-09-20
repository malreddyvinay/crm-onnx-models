# Comparing Approaches for Power Apps Notifications: Why JavaScript Is the Best Solution

In this blog, we’ll explore different approaches to implementing dynamic notifications in Power Apps model-driven apps, specifically for notifying users. By comparing JavaScript, Business Rules, and Power Fx, we’ll determine which is the best-suited solution for our scenario. Our requirement involves displaying a notification with a 5-second timeout when the linked Address is Inactive, ensuring a seamless user experience. Spoiler: JavaScript emerges as the most flexible and powerful choice. Let’s dive into the details to understand why.

## The Requirement

Our Power Apps model-driven app uses two Dataverse tables:

- **Address** : Contains address records with a status (`statecode` and`statuscode` ), where Active is`statecode = 0` and Inactive is`statecode = 1` (e.g.,`statuscode = 2` for “Inactive/Retired”).
- **Site** : Includes a lookup field (`cr123_addressid` ) linking to an Address record in a one-to-many relationship.

We needed to:

1. Create a system view in the Site table to show Sites linked to Inactive Addresses.
2. Display a notification on the Site main form when the linked Address is Inactive, suggesting an Active Address, with the notification clearing after 5 seconds.

We implemented the system view using the Power Apps maker portal’s view designer, filtering for Sites with an Inactive Address (`statecode = 1`). For the notification, we evaluated JavaScript, Business Rules, and Power Fx to find the best approach.

## Approach 1: JavaScript Solution

The JavaScript solution uses a web resource attached to the Site form’s OnLoad event to check the Address status and display a notification. Here’s the code:

```
// Function to display a notification if the related Address is Inactive
// Ensure schema names and status codes are updated:
// - Replace 'cr123_addressid' with the actual Address lookup field schema name
// - Replace 'cr123_address' with the actual Address table logical name
// - Replace '1' with the actual statecode for Inactive (typically 1)
// - Replace '2' with the actual statuscode for Inactive reason (e.g., Inactive/Retired)
function showInactiveAddressNotification(executionContext) {
    var formContext = executionContext.getFormContext();
    
    // Check if running on the main form (2 = Update form)
    if (formContext.ui.getFormType() !== 2) {
        return;
    }
    // Get the Address lookup field
    var addressLookup = formContext.getAttribute("cr123_addressid");
    if (!addressLookup || !addressLookup.getValue()) {
        // Clear any existing notification if no Address is selected
        formContext.ui.clearFormNotification("InactiveAddressWarning");
        return;
    }
    // Get the Address ID
    var addressId = addressLookup.getValue()[0].id;
    // Retrieve the Address record's statecode and statuscode
    Xrm.WebApi.retrieveRecord("cr123_address", addressId, "?$select=statecode,statuscode").then(
        function (result) {
            // Clear any existing notification
            formContext.ui.clearFormNotification("InactiveAddressWarning");
            // Check if Address is Inactive
            if (result.statecode === 1 && result.statuscode === 2) {
                // Set notification
                formContext.ui.setFormNotification(
                    "The related Address record is Inactive. Please consider selecting an Address with Active status.",
                    "WARNING",
                    "InactiveAddressWarning"
                );
                // Clear notification after 5 seconds
                setTimeout(function() {
                    formContext.ui.clearFormNotification("InactiveAddressWarning");
                }, 5000);
            }
        },
        function (error) {
            console.log("Error retrieving Address: " + error.message);
            formContext.ui.setFormNotification(
                "Failed to verify Address status. Please try again or contact support.",
                "ERROR",
                "AddressError"
            );
            setTimeout(function() {
                formContext.ui.clearFormNotification("AddressError");
            }, 5000);
        }
    );
}
// Optional: Add OnChange handler for dynamic updates
function registerAddressLookupOnChange(executionContext) {
    var formContext = executionContext.getFormContext();
    var addressLookup = formContext.getAttribute("cr123_addressid");
    if (addressLookup) {
        addressLookup.addOnChange(showInactiveAddressNotification);
    }
}
  
```
  ### How It Works

- **OnLoad Event** : Runs on form load, ensuring it only executes on the main Update form (`formType = 2` ).
- **Lookup Check** : Verifies the Address lookup field (`cr123_addressid` ) has a value, clearing notifications if empty.
- **Web API Query** : Fetches the Address’s`statecode` and`statuscode` via`Xrm.WebApi` .
- **Notification** : Displays a banner notification for Inactive Addresses, clearing after 5 seconds via`setTimeout` .
- **Dynamic Updates** : Attaches an OnChange handler to the Address lookup for real-time updates.
- **Dependencies** : Ensures the`cr123_addressid` field is available via a table column dependency.

### Implementation Steps

1. Create a JavaScript web resource (`new_showInactiveAddressNotification` ) with the code above, updating schema names.
2. Add the web resource to the Site form’s Form Libraries and register both functions under OnLoad, enabling “Pass execution context.”
3. Add a dependency for `cr123_addressid` .
4. Test across scenarios (Inactive Address, Active Address, no Address, lookup changes).

## Approach 2: Business Rules

Business Rules provide a no-code way to apply form logic, such as showing error messages or locking fields.

### Limitations

- **Intrusive Messages** : Error messages block form saving, unlike JavaScript’s non-intrusive banner notification.
- **Limited Logic** : Cannot query related records’`statecode` /`statuscode` or implement timeouts.
- **Static Behavior** : Lacks support for dynamic updates on field changes without form reloads.

### When to Use

Business Rules suit simple, no-code tasks (e.g., locking fields) but are inadequate for dynamic notifications.

## Approach 3: Power Fx

Power Fx is a low-code formula language used in canvas apps and some model-driven app features (e.g., command bar rules).

### Limitations

- **No OnLoad Support** : Power Fx cannot run on model-driven form OnLoad events, which rely on JavaScript’s`Xrm` API.
- **Custom Page Needed** : Requires a modal custom page, which is intrusive and complex to integrate.
- **No Native Notification** : Power Fx’s`Notify` function doesn’t support form banner notifications in model-driven apps.
- **Integration Complexity** : Combining Power Fx with JavaScript for form events adds unnecessary overhead.

### When to Use

Power Fx is ideal for canvas apps or command bar logic but unsuitable for model-driven form events.

## Why JavaScript Is the Best-Suited Solution

JavaScript outperforms Business Rules and Power Fx due to its unmatched flexibility and capability:

### 1. Comprehensive Feature Support

- Handles all requirements: notification, timeout, and dynamic updates within a single script.
- Uses `setFormNotification` for native banner notifications that integrate seamlessly with the app’s UI.

### 2. Advanced Logic and Integration

- Queries related records via `Xrm.WebApi` for dual`statecode` /`statuscode` checks.
- Supports OnChange handlers for real-time updates, unlike Business Rules.
- Integrates with model-driven app forms via the `Xrm` API.

### 3. User Experience

Delivers a polished experience with non-intrusive notifications and precise timeout control.

### 4. Robustness and Extensibility

- Includes error handling for Web API failures and form type checks for compatibility.
- Supports accessibility (e.g., can add `aria-label` for screen readers).
- Maintains reliability with table column dependencies.

Compared to Business Rules’ limited scope and Power Fx’s inapplicability to form events, JavaScript’s versatility makes it the clear winner.

## Conclusion

By exploring JavaScript, Business Rules, and Power Fx for our Power Apps notification requirement, we’ve seen that JavaScript is the best-suited solution. Its flexibility, integration with model-driven app forms, and ability to handle complex logic and dynamic updates make it far superior to the limited Business Rules and incompatible Power Fx. This solution enhances user awareness, ensures data integrity, and delivers a seamless experience in our app. Try it in your Power Apps project and see the difference!

What’s your preferred approach for Power Apps notifications? Share your insights in the comments!

## No comments:

## Post a Comment