This article explains how to update the lookup field display name in Dynamics 365 with JavaScript. The steps involve adding a JavaScript function that retrieves related record and fields from the related table, and updating the display name accordingly. The function can be added to the on-change and on-load events of the form, and the changes will only be reflected on the record referencing the lookup record. The article also includes examples of the JavaScript code for adding both the product name and number or only the product number as the display name.

### Table of Content

- Update Lookup Display Name with JavaScript
- How to Add the JavaScript Function to the Form
- Conclusion
- Resources

### Prerequisites

- Familiar with Dynamics 365
- Familiar with JavaScript

## Update Lookup Display Name with JavaScript

In this example, we look at how we can update the lookup field display name of the product table in Dynamics 365 with JavaScript. By showing the product number in addition to the name of the product, or only the product number. In the image below the default display name of the product table lookup field is shown and this is what we want to change.

By using JavaScript we change the display name by adding the product number in addition to the product name as seen below.

The JavaScript example below shows how to add the product number in addition to the product name in the lookup field as seen in the image above.

```
var sdk = window.sdk || {};
(function () {
    "use strict"
    this.setProductDisplayName = async function (executionContext) {
        const formContext = executionContext.getFormContext();
        let productColumn = formContext.getAttribute("productid");
        let productValue = (productColumn === null) ? null : productColumn.getValue();
        if (productValue !== null) {
            let productId = productValue[0].id.replace(/{|}/g, "");
            await Xrm.WebApi.retrieveRecord("product", productId).then(
                function success(result) {
                    if (productValue[0].name === result["name"]) {
                        productValue[0].name = `${result["productnumber"]} ${result["name"]}`
                        productColumn.setValue(productValue);
                    }
                },
                function (error) {
                    console.log(error.message);
                }
            );
        }
    }
}).call(sdk);
```
Moreover, we can remove the product name and only use the product number like below.

And the JavaScript code for setting the product number as the display name is the one below.

```
var sdk = window.sdk || {};
(function () {
    "use strict"
    this.setProductDisplayName = async function (executionContext) {
        const formContext = executionContext.getFormContext();
        let productColumn = formContext.getAttribute("productid");
        let productValue = (productColumn === null) ? null : productColumn.getValue();
        if (productValue !== null) {
            let productId = productValue[0].id.replace(/{|}/g, "");
            await Xrm.WebApi.retrieveRecord("product", productId).then(
                function success(result) {
                    if (productValue[0].name === result["name"]) {
                        productValue[0].name = `${result["productnumber"]}`
                        productColumn.setValue(productValue);
                    }
                },
                function (error) {
                    console.log(error.message);
                }
            );
        }
    }
}).call(sdk);
```
## How to Add the JavaScript Function to the Form

To change the display name on change and on load we need to add the JavaScript function to the on-change event and the on-load event on the form. For a more detailed explanation of how to add a new JavaScript web resource and how to add it to the form check out this article, https://fredrikengseth.com/how-to-add-javascript-to-form-on-load-in-dynamics-365/

First, add the web resource to the form library like below.

Then, add the function to the on-change event on the Product column on the form.

Finally, add the function on the on-load event of the form.

## Conclusion

In conclusion, changing the display name on lookup fields in Dynamics can be accomplished by utilizing JavaScript to retrieve related records and other fields from the related table. This technique allows for the display name to be updated without altering the value in the primary field of the related record, and the changes will only be reflected on the record referencing the lookup record. Check out the gif below to see what it looks like.

## Resources

- https://learn.microsoft.com/en-us/power-apps/developer/model-driven-apps/clientapi/reference/xrm-webapi/retrieverecord
- https://learn.microsoft.com/en-us/power-apps/developer/model-driven-apps/clientapi/reference/attributes/setvalue
- https://www.hellosmart.ca/2022/12/tips-change-lookup-field-display-name.html