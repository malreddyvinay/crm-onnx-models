# Flow Checker Recursive Loop

On 27th March 2023 the solution checker was updated to include the warnings and errors output by the Flow Checker. Let’s investigate the flow checker warning *‘Actions in this flow may result in an infinite on trigger loop. Please ensure you add appropriate conditional checks to prevent this flow from triggering itself.’* (`flow-avoid-recursive-loop`).

What does it mean? How can one resolve the warning, especially when working with Dataverse? Let’s investigate.

## Infinite Trigger Loop

This warning will be output when a flow uses the Dataverse Trigger in combination with a Dataverse action in the same flow. Specifically

| Trigger Change Type | Action | 
|---|---|
| Added | Add a row | 
| Added or Deleted | Add a row, Delete a row | 
| Added or Modified | Add a row, Update a row | 
| Added or Modified or Deleted | Add a row, Update a row, Delete a row | 
| Deleted | Delete a row | 
| Modified | Update a row | 
| Modified or Deleted | Update a row, Delete a row | 

### Example

In the following flow when a contact is added, or when a contacts first or last name is updated we will set the nickname field to be the initials of the contact. e.g. Tom Jomes gets a nickname of TJ.

As a designer I know that this flow will not create an infinite loop on its own. However, if there were another flow that updated the first name or last name based on the initials changing all bets are off, and it’s very possible that a loop could be created.

It’s interesting to note that the flow checker warning (red dot) appears whilst the flow is being edited. The flow does not need to be saved. Clicking on the ‘flow checker’ will show details of the warning.

## Solution Checker

Since the update on 27th March this error is also output by the solution checker in the maker portal, e.g.

## Eliminating the warning

The only method that I’ve found of eliminating the warning is to split the flow into a main flow, and then a child flow that performs the update.

### Parent Flow

Only contains the trigger and then launches the child flow that updates the same record!

### Child Flow

Updates the same record as triggered in the parent flow, but because it’s in a different flow the flow checker warning is not output.

### Discussion

Whilst this eliminates the warning it’s quite an extreme step to take to stop the warning, and still it does not eliminate the risk of an infinite loop.

Most warnings emitted by the solution checker indicate that something is incorrectly setup and the customisation should be reviewed and updated so that the warning is no longer output. This is not practically possible with this warning.

## Ignoring the warning

Whilst the maker portal provides no options when the running the solution checker interactivelly it is possible to alter the severity of each type of issue using the power platform command line and associated Azure DevOps (or Github Action) Power Platform Build Tools task.

### Power Platform CLI

- First export the solution to a zip file with `pac solution export --name <solution> --path ./<solution>.zip` .
- Create a JSON file, e.g. `ruleOverride.json` , with the following contents:

```
[
  { "Id": "flow-avoid-recursive-loop", "OverrideLevel": "Informational" }
]
```
- Run the power platform checker: `pac solution check --path .\<solution>.zip --ruleLevelOverride .\ruleOverride.json` .  An output similar to below will be produced:

We can seee that the `flow-avoid-recursive-loop` has been downgraded in severity to `Informational` (from the default value of `Medium`).

### Power Platform Build Tools

Use the ‘Rules to Override’ property of the Power Platform Checker task in the Power Platform Build Tools with value `RulesToOverride: '[{ "Id": "flow-avoid-recursive-loop", "OverrideLevel": "Informational" }]'`

e.g

## Thoughts

Personally, I feel this is a design time warning. Whilst it might be useful to new makers when creating or editing a flow using the flow editor it does not help to have this warning output by the solution checker since there is no practicable way for the warning to be eliminiated.

## Conclusion

1. This warning will often be encountered, since it is common for a flow that is triggered on create, modify or delete to update the same or other records in the same table.
2. It can’t easily be removed/eliminated by changing the design of a flow. Using child flows is a good way to break up flows, but is probably overkill in many scenarios where this warning is generated.
3. We can’t eliminate the warning in the solution checker in the maker portal.
4. We can reduce the severity of the issue to ‘Informational’ when running via PAC or PAC CLI.

A goal should be for solutions to pass the solution checker with zero issues reported. With the introduction of this warning this is no longer possible, at best we can reduce the warnings to ‘Informational’ and ignore warnings of this severity.

### References

- Find and fix errors with Flow Checker
- Use solution checker to validate your model-driven apps in Power Apps

#### Avoiding flow recursion

These blogs explain how to design flows that may prevent recursion, but do not address the Solution Checker warning: