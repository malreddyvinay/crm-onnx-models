As a programmer, using Try-Catch is a common programming practice to handle exceptions. Now, since we’ve moved more towards low-code platform implementations, error handling here is a must as well.

Generally, if a Flow fails as per below, we should be able to handle the exceptions effectively –

 

And this is what happened to my action step – 

And this Flow will end in Failed Run status. So let’s ensure we handle this in a simple way.

## Group actions using Scope

First step is to club the actions into a group which can be accomplished by an action called Scope. This will give us controls as to what happens if this Scope fails, succeeds, times out or is skipped –

1. Search for Scope in the Flow and add it.
2. Now, add the actions which needs to be handled for Exceptions in the Scope you just added.
3. And it should looks like this – Also, consider renaming the Scope as you might want to handle each section of the Flow differently for different potential actions 
Here, your Try block is ready.
4. Now, let’s design the Catch block. Add one more Scope to the Flow (Ideally, after the Try Scope we just added)
5. For example, you can add an email step to notify the developer, typically.

## Configure Run After

Now, let’s configure the Run After on the ‘**Catch SP Exceptions**‘ scope we added in the step above

1. Now, go to the ellipses on the Catch scope we just created.
You’ll find Configure Run After. This defines that when should this selected Scope Run based on the results of the previous Scopes.
2. And you can select the criteria you are defining for the ‘Try – SharePoint Actions’ scope’s results.
The below implies that run ‘Catch SP Exceptions’ block after the ‘Try – SharePoint Actions’ block failed (or any action in it fails)
3. And at this point, you are done. You can see a little i icon to see what is configured.
The arrow connecting the steps are also different (in brown as compared to other black/dark gray arrows.)

## Testing

Now, let’s test this simple scenario and see how the executions will take place in terms of error.

1. We’ll resubmit the same failed Run to now go through these Scopes and observe our course of action.
 As you see below,**Try – SharePoint Actions** scope has failed as expected but because we had configured the**Catch SP Exceptions** to**Run After** the**Try – SharePoint Actions** failed.
 And note that the End Result of the Flow is also a**Success** .
2. Now, let’s see what happens if the Exception doesn’t occur and it succeeds.
 But, notice that even the steps after the**Catch SP Exceptions** didn’t execute.
Now, I’ll explain below why that happened.
3. This happened because **Catch SP Exceptions** itself didn’t execute and the Delay step is connected to**Catch SP Exceptions** steps by default.
 Now, you’ll need to also configure the**Delay** Step to Run After the**Try – SharePoint Actions** is**Skipped** executed. Then, the Flow will continue it’s normal execution that point on.
4. And if you Run this again, since the **Catch SP Exceptions** is**Skipped** , the Delay will continue to Run.
And everything after that. See another step added to validate this.

Hope this was quick and easy to understand.

Here are some more Dynamics 365 posts which you might be interested in –

Thank you!!

good and easy explanation with all details

Thank you, Sudhindra!