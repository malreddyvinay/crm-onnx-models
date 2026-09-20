## Where we Left Off

Last week, we spoke about some of the basic Power Platform security concepts we’re mostly familiar with.

In today’s blog, we’re discussing how to assign Entra ID security groups to environments, reviewing how this drives user access, and taking a crack at the force sync user action to help speed up user synchronisation between Entra ID and environment users.


## Creating a New Environment

As I’m sure you’re familiar with, when creating a new environment, you’re advised to assign a security group to the environment. When you click on add, you have the choice to select none, but by doing so, only users with various admin roles assigned will sync to the environment, and additional users would need to be assigned manually.

In this scenario, the environment I’m creating is specific to the Avengers. I’ve currently got an Entra ID security group setup with Steve, Tony, and Thor as members. The security group, as seen below, is called The Avengers. How original.


Back in the Power Platform admin panel, where I am creating their new environment, I’ve selected The Avengers from my list of security groups and am ready to finalise the environment.



## Some Bumps on the Ride

Now, when users are added to the Entra ID group, in a perfect world, those users should sync to the environment and grant them access. In most scenarios, this is the case. However, there are times where the sync is just slow, or there are some caching issues, and the users you need to show up just don’t show up quick enough! I can be an impatient person at times, so this definitely frustrates me.

Often, the user needs to first log into the environment for their profile to sync, but when you are onboarding multiple users at a time, you probably just want to see them in the environment and start assigning some roles (another post for another time ).



## Playing With the Force

Don’t hate on me; I know I’m referencing two completely different universes, but it’s the concept that matters, right ?

When it comes to the Power Platform, there’s always a way of streamlining a process through workflows and automation. Whether it’s record creation, record assignment, or, in this case, syncing users. There’s always a way.

Because I’m impatient and I’ve had scenarios where I’ve been in loops of regression testing, I go straight to the Force Sync Users action in Power Automate. I’ve created a straight-forward manual flow that syncs users from an Entra ID group to an environment. I’m not the first to do this, and I definitely am not the last. This type of flow would be a must-have when you are building a security model or RBAC model based on Entra ID security groups.

As a start, the flow is triggered manually for demonstration purposes. We will update this shortly. Next, I’ve added the Entra ID “Get group members” action. Based on the group ID I provide; this action will query the group ID and return all the members belonging to that group. In this scenario, I am querying the Avengers group, so it should return 3 users.

The next action is called Force Sync User and is found under the Power Platform for Admins action. If I select my environment as The Avengers and place the output of group member ID from the previous action into the ObjectId field, this action will then force synchronise the Entra ID user to Dataverse if the changes made have not yet reflected.

Now if I run this flow manually, you can see it successfully returns the three members of the group, and it has also force synced them to the new environment.



## Planning Ahead

Now that the foundation is complete, I can scale it up a bit to make this process a bit more streamlined.

I’ve updated the flow to be triggered by an event, specifically, by the Office 365 Group “When a group member is added or removed.” Similar to before, I simply add the group ID to the Group ID field, update the fields in my Force Sync action to now be the outputs of the new trigger, and Bobs my uncle (quite literally .)


If I head back to The Avengers Entra ID group and add, say, Mr. Bruce Banner, my Force Sync User flow should auto-trigger once I add Bruce and should sync him to the environment within a couple of seconds.



## Simplicity Evolving into Operational Harmony

This is a very straightforward and simple process. As Power Platform developers, we are mostly all aware of assigning Entra ID security groups to environments and creating Force Sync flows. The capability is not in the idea, but in the scalability.

Think bigger. You’re the administrator of an organisation with 3,000 active users, all members of various security groups that govern environment access, security roles, business unit assignment, and more. Managing these users manually every time you have to add, remove, or change groups will turn into a full-time job on its own. I’ll touch on this a bit more later on, but streamlining Teams and security groups driven by Entra ID security groups becomes seamless. Update a group in one location, and let your flows do the rest of the work.

It’s just one more step forward towards operational harmony.