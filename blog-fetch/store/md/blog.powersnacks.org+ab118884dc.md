# Efficient Flows - Remapping Known Null Values in an Array

#NoApplyToEach #NoVariables

Power Platform Consultant with an unhealthy obsession with Crabs.

A tech enthusiast for as long as I could walk (and hey, maybe even before that!). I'm passionate about all aspects of technology, whether it's Hardware, Software or emerging technologies.

I've long had a passion for coding and have finally made it a career-reality specialising in Microsoft Power Platform. I also dabble in JavaScript, C# and PowerShell. I've even been known to have a stab at some older languages/compilers.

I've spent my career repairing Printers and Photocopiers, Managing Printer Fleets and configuring document workflow solutions.

I've recently started public speaking, and I'm eager to share my insights and knowledge with everyone.

## The Problem

I recently had a requirement to filter an array coming back from a flow based on a field being blank. This isn't usually an issue when returning data directly from a data source in a Canvas App/Custom Page as null values are represented as Blank(). However, we needed to return data from a flow due to the volume of records being returned.

As an example for this post, I'm going to work with this simple array:

```
[
  {
    "Value1": "Crab"
    "Value2": "House"
  },
  {
    "Value1": null,
    "Value2": "Crab"
  }
]
```
Note in this array, we have two properties that are strings. However, note that Value1 is also **null** in the second object, so technically Value1 could be two different data types.

If we go ahead and automatically generate the JSON schema for this in the Parse JSON action, we get the following schema generated:

```
{
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "Value1": {
                "type": "string"
            },
            "Value2": {
                "type": "string"
            }
        },
        "required": []
    }
}
```
## Schema issues

The Generate Schema function returns the topmost schema values in this array. As such both properties are identified as strings. If we execute this flow now, the following error occurs:

```
[
  {
    "message": "Invalid type. Expected String but got Null.",
    "lineNumber": 0,
    "linePosition": 0,
    "path": "[1].Value1",
    "schemaId": "#/items/properties/Value1",
    "errorType": "type",
    "childErrors": []
  }
]
```
With JSON schemas in Power Automate, it's possible to specify more than one data type for a property in the schema.

```
{
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "Value1": {
                "type": ["string", "null"]
            },
            "Value2": {
                "type": "string"
            }
        },
        "required": []
    }
}
```
Note we're now specifying an array of types for Value1, including Strings and Nulls

With the new schema, the JSON now validates.

## Returning Nulls to Canvas Apps

So here comes the issue, if we want to return this to a Canvas App, the Canvas App Studio can't interpret the WADL (Web Application Description Language) definition when null values are specified:

In the above example, we're using the Response action to return a Dataverse array to a Canvas App.

If we now try and import the flow into a Canvas App, we get this dreaded message about WADL schema:

**In essence, we can't pass potentially null values back to a Canvas App.**

So if we know we might be getting null values, and we need a way to return blank values to our Canvas App, what could we do? 🤔

## Select, SetProperty, Coalesce

I've found an efficient way to replace null values in known fields with empty strings by combining the Select action, setProperty formula and Coalesce:

## How to:

Add a select action after Parse JSON, and specify the JSON output body as your "from" property in Select:

Now change the Map property from key/value mode to text mode:

And finally, in the Map property, set the following formula:

```
setProperty(item(), 'Value1', coalesce(item()?['Value1'],''))
```
*replace Value1 with your corresponding Value*

In this formula, we're updating the current object's Value1 property in the array (as "Select" is iterating over the entire array, no Apply to Each required!) with the output of the Coalesce function, which either returns the string contents of Value1, or Null. Coalesce will use the next available argument as a value if the first value is Null. So in essence, replacing a null value with an empty string.

The output of Select can now be passed to the Response action, and is WADL compliant! 🦀

This solution omits the need for any Apply to Each action to iterate over the array. Using the Select function allows us to perform that iteration far more efficiently.

**But what do you think? I'd be interested to see if you have a different or better approach for this. Comment below if you do!**

**Next Time:** We'll take a look at how we can remove variables from our flows to help with performance gains!