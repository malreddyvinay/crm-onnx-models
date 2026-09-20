# Power Automate – End flow using Terminate

3 use cases

Introduction:

Do you want to just test a portion of your flow without having to remove your other actions? Here are some use cases for the **Terminate** action in Power Automate.

Use Case 1:

You can use **Terminate** to test a portion of the flow. The flow will run from the trigger to the **Terminate** action. This can be useful if your flow has many calculations or conditions at the upper portion and then actions that send emails at the bottom portion. In this case, you do not want to send emails every time you test, but just want to see the results of the calculations. You may use **Terminate** to stop the flow up to a specified point.

Use Case 2:

You may use **Terminate** inside a condition group. If a condition is met or unmet, you can use **Terminate** so that it will not proceed with the actions below it.

Use Case 3:

You can stack condition groups below each other. Whenever a condition is not met, you can use **Terminate** to end the flow. This can be an alternative to the nested condition groups.

Note:

If you use **Terminate** on parallel branches, the flow will stop all branches once the **Terminate** action has been reached.

Did this article help? Let us know how we can improve. Send us a message by clicking the “Contact Us” button below.

Article last updated on May 17, 2024

Need expert guidance on Power Apps?