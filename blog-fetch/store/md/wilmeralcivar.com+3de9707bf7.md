# From Basics to Brilliance: TypeScript Examples for Model Driven Apps

This is the last of a blogpost series on how to apply TypeScript in Model Driven Apps, In my previous blogpost I’ve explained how to create a TypeScript project in Visual Studio for Model Driven Apps, in this blogpost I will show you some basic examples but also other 3 cool examples in order to open a Custom Page, call Custom API and call a Clow Flow.

The idea is you can re-use this code in your projects and of course changing it a bit according to your requirements.

Without further introduction let’s begin.

## Basic examples

I have already lost count of the times I have had to apply some basic logic in main forms, and when I say basic logic I mean that depending on certain conditions I have to make some fields mandatory or not, or depending on these conditions I have to hide or show a field.

Or it could even be retrieving a related record and setting a search field with the retrieved related record, well these are very common scenarios in projects. Having said that just to give you some context this code applies to the main form of the account.

The following code is divided into sections, the first part is to show how to retrieve the value of different columns where the data type is different like string, number, option set, lookup, date.

In the second part I am using Dataverse web API to retrieve a single record in this case I am retrieving an account with its name and its main contact which is a lookup field. Then I am setting the primary contact field with the search contact of the retrieved account.

And finally in the third part I am making one field required and making another field hidden:

###### const formcontext = executionContext.getFormContext();

 

 //retrieve values from the form

 const exampleLookup: Xrm.Attributes.LookupAttribute = formcontext.getAttribute<Xrm.Attributes.LookupAttribute>(‘primarycontactid’);

 const exampleString = formcontext.getAttribute<Xrm.Attributes.StringAttribute>(‘websiteurl’).getValue();

 const exampleDateTime = formcontext.getAttribute<Xrm.Attributes.DateAttribute>(‘column_schema_name’).getValue();

 const exampleOptionset = formcontext.getAttribute<Xrm.Attributes.OptionSetAttribute>(‘industrycode’).getValue();

 const numberOfEmpAtt = formcontext.getAttribute<Xrm.Attributes.NumberAttribute>(‘numberofemployees’);

 

//retrieve the record GUID

 const recordId = formcontext.data.entity.getId();

 //use the Web API to retrieve a single record

 const accountData = await Xrm.WebApi.retrieveRecord(‘account’, recordId, ‘?$select=name,_primarycontactid_value’);

 const contactId = accountData[‘_primarycontactid_value’];

 const contactName = accountData[‘_primarycontactid_value@OData.Community.Display.V1.FormattedValue’];

 //create a lookup object

 const lookupData: Xrm.LookupValue[] = [{ id: contactId, entityType: “contact”, name: contactName }];

//set a lookup in the form

 formcontext.getAttribute<Xrm.Attributes.LookupAttribute>(‘primarycontactid’).setValue(lookupData);

 

 //set required level

 let getAttribute: Xrm.Attributes.Attribute<any> = formcontext.getAttribute<Xrm.Attributes.StringAttribute>(‘websiteurl’);

 getAttribute.setRequiredLevel(“required”); //or none to make not required

 

 //show or hide a column

 let uiAttribute: Xrm.Controls.StandardControl = formcontext.getControl<Xrm.Controls.NumberControl>(‘industrycode’);

 uiAttribute.setVisible(false); //or true to make it visible

## Open a Custom Page

This scenario is becoming more and more common in projects, to achieve this it is recommended to have a button in the ribbon of the main form you want and when you click on that button you can trigger the following code to open the desired custom page, the best thing about this code is that it is generic so it can be used for every Custom Page you have:

###### export async function OpenCustomPage(primaryControl: Xrm.FormContext, customPageName: string): Promise<Xrm.Navigation.CustomPage>

{

    const recordId: string = primaryControl.data.entity.getId().replace(“{“, “”).replace(“}”, “”);

   

    return new Promise<Xrm.Navigation.CustomPage>(function (resolve, reject)

    {

        const navigationOptions: Xrm.Navigation.NavigationOptions = {

            target: 2,

            position: 1,

            width: { value: 50, unit: “%” },

            height: { value: 50, unit: “%” },

            title: “Custom Page title you want to show to the user”

        };

 

        const customPage: Xrm.Navigation.CustomPage = {

            pageType: “custom”,

            name: customPageName,

            entityName: primaryControl.data.entity.getEntityName(),

            recordId: recordId,

        };

 

        Xrm.Navigation.navigateTo(customPage, navigationOptions).then(

            function (success) {

                primaryControl.data.refresh(false);

                resolve(success);

 

            }).catch(

                function (error) {

                    console.log(‘Error: ‘, error);

                }

            );

    });

}


You can create the button using the new command designer or you can use the classic and beloved ribbon workbench like I did for this example:

## Call a Custom API

This is my favorite one, Custom APIs are like plugins on steroids, it’s backend code in which you can do whatever you want and the best thing is that you can call this code from other parts of the platform like canvas app, Custom Page, Clow Flow, Custom Connector or from a button.

###### export async function CallCustomAPI(primaryControl: Xrm.FormContext) : Promise<Xrm.ExecuteResponse>

{

    const recordId : string = primaryControl.data.entity.getId().replace(“{“, “”).replace(“}”, “”);

 

    Xrm.Utility.showProgressIndicator(“processing…”);

    return new Promise<Xrm.ExecuteResponse>(function (resolve, reject) {

        const execute_name_of_your_custom_apip_Request = {

            // Parameters

            Name_of_your_input_parameter: recordId, // Edm.String

 

            getMetadata: function () {

                return {

                    boundParameter: null,

                    parameterTypes: {

                        Name_of_your_input_parameter: { typeName: “Edm.String”, structuralProperty: 1 }

                    },

                    operationType: 0, operationName: “name_of_your_custom_api”

                };

            }

        };

 

        Xrm.WebApi.online.execute(execute_name_of_your_custom_apip_Request).then(

            function success(response) {

                if (response.ok) {

                    response.json().then(function (results) {

                        const OutputParameter1 = results[“OutputParameter1”];

                        const OutputParameter2 = results[“OutputParameter2”];

                        const OutputParameter3 = results[“OutputParameter3”];

                    });

                    resolve(response);

                }

            }

        ).then(function (responseBody) {                

            Xrm.Utility.closeProgressIndicator();

        }).catch(function (error) {

            console.log(‘Error: ‘, error);

            Xrm.Utility.closeProgressIndicator();

            reject(error);

        });

    });

}

You can create the button using the new command designer or you can use the classic and beloved ribbon workbench like I did for this example:

Here’s a tip, you can use the Dataverse Rest Builder plugin from XRMToolbox to create in a few clicks all the code you need to call the Custom API, here you have another blogpost where I explain in detail how to create the Custom Page, how to create the button and how to use Dataverse Rest Builder to create the code that will call the Custom Page:

## Call a Clow Flow

This one is very common, an example could be triggering an approval process (the cloud flow) by clicking a button, it is worth mentioning the cloud flow must be an Http trigger:

And here is the code:

###### export async function callFlow(primaryControl: Xrm.FormContext, flowurl: string): Promise<string>

{

    const recordId: string = primaryControl.data.entity.getId().replace(“{“, “”).replace(“}”, “”);

    const userId: string = Xrm.Utility.getGlobalContext().userSettings.userId.replace(“{“, “”).replace(“}”, “”);

 

    Xrm.Utility.showProgressIndicator(`In Progress…`);

 

    const myHeaders = new Headers();

    myHeaders.append(“Content-Type”, “application/json”);

 

    const raw = JSON.stringify({

        “topcount”: 10,

        “skipcount”: 1,

        “recordId”: recordId,

        “userId”: userId

    });

 

    const requestOptions: RequestInit = {

        method: ‘POST’,

        headers: myHeaders,

        body: raw,

        redirect: ‘follow’

    };

   

    return new Promise<string>(async function (resolve, reject) {

        fetch(flowurl, requestOptions)

            .then(response => response.text())

            .then(result => function () {

                console.log(result);

                Xrm.Utility.closeProgressIndicator();

                resolve(result);

            })

            .catch(error => function () {

                console.log(‘error’, error);

                Xrm.Utility.closeProgressIndicator();

                reject(error);

            });

    });

}

Here is another tip you can use Postman to trigger your cloud flow and then on the top right corner you can see the JavaScript code that you can copy and paste it in your project of course you will have to change it a bit because this is a TypeScript project:

## Conclusion

There you have it, some cool TypeScript examples to solve common requirements, of course you can make this code even more bullet proof. For example the call to the cloud flow method where as you have seen the second parameter is the URL of the cloud flow, well a good practice would be to send as second parameter the name of an environment variable and inside the TypeScript method you can retrieve the value of the environment variable which will be the actual URL of the cloud flow.

To retrieve the value of the environment variable you can use a retrieveMultiple using a fetchXML.

There are many other scenarios where TypeScript can be applied such as filtering a lookup field or opening a related record as a pop up modal.

In any case I hope you enjoyed this blogpost as much as I enjoyed doing it.

Hello there! Welcome to my blog!

My name is Wilmer Alcivar and I’m a Power Platform fan

I’d love to share my knowledge, so please do not hesitate to connect!