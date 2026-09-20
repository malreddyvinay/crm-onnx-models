**Introduction**:

In the dynamic landscape of modern business operations, effective communication stands as a cornerstone for achieving success. Within Dynamics 365 CE, various communication avenues are available to engage with customers through activities. While the platform offers several out-of-the-box options for sending notifications to customers, there are occasions when we must extend the capabilities of Dynamics 365 CE to meet specific requirements.

Consider a scenario where the need arises to dispatch emails using templates for a custom entity. This email correspondence must originate from a designated Queue and be directed to unresolved email addresses. In this first post, we will discuss about sending emails to custom entities utilizing templates within Dynamics 365 CE.

**Details**

Email templates in Dynamics 365 CE are like pre-made layouts for emails that help businesses send messages to customers in a consistent and efficient way. With templates, companies can keep their brand style the same and make sure their messages are interesting to customers. While creating email template we have only few out of the box entities available directly, for other out of the box entities or custom entities we need to select Global option.


While creating email template for the above available out of the box entities for example let’s say Account, we can easily use dynamic values options like below and use data field to design our template.


But we can’t use these options for our custom entities, while we are using Global template we can only add dynamic values from the User entities directly but this does not mean we can’t use dynamic values from our custom entity, yes we can do that 🙂 using following options.

Let’s take an example we want to use dynamic value for the primary field from our custom entity, we need to write is using following syntax

{!entitylogicalname:fieldlogicalname;}

so for example if we have a him_event entity and we want to use dynamic value for name field (him_name) we need to write it like below

{!him_event:him_name;}

Similarly let’s we have field for other data type like below


In above screenshot we cost is currency field, event organizer is lookup field and event type is an option set. When we will save these change it should be changed like below


If it is not changing like above it means there is some issue in the syntax. Now let’s say we want to bring some non primary fields from the lookup entity, we don’t have any out of the box option available so in our next post we will discuss how we can bring non primary field to our email while using Global templates so stay tunned.

**Summary**

Today’s we saw how we can use dynamic values for our custom entity in the global template.

Hope it will help someone !!

**Keep learning and Keep Sharing !!**