| Muhammad Yaseen

Microsoft power automate flow did not triggered on Association/Disassociation of an entity.so for this purpose we can use Web hook to trigger our automate flow on Association/Disassociation of specific entity and on specific relationship.

Firstly create the Http flow.

On setting of this connector write the trigger condition

Write your relationship name here

Then in plugin registration tool create a connection and choose your environment

Then click on register new webhook

Brake your flow URL like mentioned below

Add step for Associate/Disassociate for

Entity filtering is not supported on these messages so you will have to listen for all of them.

The flow will now fire every time when a record is associated or disassociated.

Join us next time, as we continue our journey of learning canvas apps.Click here to learn more about Imperium's Power Apps Services. We hope this information was useful, and we look forward to sharing more insights into the Power Platform world.