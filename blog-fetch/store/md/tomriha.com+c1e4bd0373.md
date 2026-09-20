*“I need to know asap if my Power Automate flow failed, I can’t wait a week for it to send the error message or check daily the flow run history.”*

One of the Power Automate features is a basic error handling process, a weekly email that will show you all the failed flows from the last week. You don’t need to configure anything for this email, the Power Automate platform sends it automatically.

But I think it has too many limitations. Firstly, only the main flow owner receives the email, not all owners. Secondly, it contains only the flow name and number of failed runs, without a link to the runs. And thirdly, it’s sent only once a week. Not many users are willing to wait for more than a week for a single flow run. That’s why it’s better to manually add an instant error message into your flow.

## Enclose your flow in ‘Scope’ action

The most important action for error handling is the ‘Scope’ action. It’s an action to encapsulate other actions, allowing you to create multiple logical sections in your flow. For the error handling you’ll need 2 of them, one ‘Scope’ for the flow and one for the ‘Error handling’.

### ‘Scope’ with flow

The first ‘Scope’ action should contain your whole flow, excluding ‘Initialize variable’ actions (they must be on top level). The benefit of this approach is that you don’t need to check every action separately. If the actions are in a ‘Scope’, you can check just the ‘Scope’ status to see if any action has failed.

As an example, if ‘Get items 2’ or ‘Get user profile (V2)’ action below fails, the whole ‘Scope – Flow’ action will fail.

### ‘Scope’ for error handling

Once you have the whole flow in the ‘Scope’ (- Flow), you can add the second one for error handling.

You must ‘Configure run after’ for ‘Scope 2’ (- Error handling) to run only if the ‘Scope’ (- Flow) has failed. That’s only if any action in the ‘Scope’ (- Flow) failed. It’s the same setting you can use as a workaround to disabling part of a flow, but this time it’s used for the intended purpose.

Then you can define in the ‘Scope 2’ what should happen next.

## Send link to the flow

You can send a link to the flow in an email or as a Teams message with the expression below.

`concat('https://flow.microsoft.com/manage/environments/', workflow()?['tags']['environmentName'], '/flows/', workflow()?['name'], '/runs/', workflow()?['run']['name'])`
#### Send the error information

You can also include name of the failed action and the error message. The result of ‘Scope’ action can be accessed with the result(…) expression.

```
result('<ScopeName>')
all spaces in the action name are replaced by _, e.g. 'Scope - Flow' will be 'Scope_-_Flow'
result('Scope_-_Flow')
```
It’ll contain all the actions in the ‘Scope’, the Succeeded, Skipped and Failed ones. Since you’re interested only in the Failed actions, you can filter them out. Take the whole result(…) array and filter only actions with status: Failed.

`item()?['status']`
‘Select’ only the relevant information from the failed actions: the action name and the error message.

```
item()?['name']
item()?['error']?['message']
```
And add the ‘Select’ output into the email or a Teams message.

`outputs('Select')?['body']`
#### End the ‘Scope 2’ (- Error handling) with the ‘Terminate’ action.

The last step is to enforce the ‘Failed’ outcome of the whole flow using the ‘Terminate’ action. If you end by sending the message, the whole ‘Scope 2’ (- Error handling) will end with a success. That means that the whole flow will end with a success. But it didn’t end with a success, there was an error during the flow run.

## Summary

When you build a flow you should always consider also the error handling part. It’s never good if other users notice that your flow is not working before you do, and I think that’s exactly what can happen if you rely only on the basic email. That’s why it’s better to add a few more actions to your Power Automate flow to send a message if the flow failed.

The solution above is using expressions to navigate the results JSON action to process the results. It’s a simplified solution to get only the failed action name and the error message, but you can get much more information. If you store the result(…) into a ‘Compose’ action, you can use it as a payload for ‘Parse JSON’ to see all the available data.

But I believe that the most important part is the link to the flow run. You don’t need to search in the run history, you get a direct link that will tell you everything. Just make sure that the recipient of the message is one of the flow owners.

Nice. We use a very similar process but post to a Team, so if multiple staff should be notified, we can just add them to the Team.

We didn’t have a link to the run itself, though. That is super useful, so I’m going through and adding it to our flows now.

Very helpful explanation, thank you! I have added this successfully to my flow. Definitely needed as the Microsoft message arrives too late, making the job of finding the faulty run almost impossible.

Genius!!! Very helpful. I am already using this approach!! Thanks

Thank you so much! This has been very helpful!