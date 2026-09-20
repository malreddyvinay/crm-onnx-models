Happy New Year, everyone! I hope you all had a fantastic holiday and winter break (yes, I get to say that to my UK network now that I am officially here). Sorry, South Africa, I do miss the beach though 🥺).

It’s been a bit rough getting back into things, purely because of the terrible two stage 👧🏼 (a blog post for another time), but nevertheless, here I am with Part 2 of understanding Solution Layers.


## Where We Left Off

My last post for 2023 discussed how unmanaged layers work within a managed solution and how developers should be very careful when it comes to deploying updates to an environment that has active unmanaged layers. I primarily focused on layers represented with a Canvas app, but today we’re exploring layers with a bit more context. forms, site maps, and a mystery involved.


## It’s Snowing Outside

The last solution I used to illustrate solution layers was a solution called “It’s Cold Outside.” Although it has been snowing in Manchester, I unfortunately could not be bothered renaming it 🙃. Anyways, in order to explore layers a bit further, I have added a few more objects to the solution, specifically a new table and a Model-Driven app. Obviously, when I created the MDA, a site map was also included in the solution.

To keep things short and sweet, I’m going to summarise the initial steps when it comes to creating unmanaged layers. If you are not familiar with how to get from an unmanaged solution to a managed solution with unmanaged layers, check out Solution Layers, Part 1 here.


### Solution Layer Process

**Step 1 – In the Dev environment**

The MDA has two pages: Weather Log and Dashboard (shown in the site map). The Weather Log table has a basic form. The solution was deployed to QA.


**Step 2 – In the QA environment**

The Status and Status Reason columns have now been added to the Weather Log form from within the MDA (a new active unmanaged layer on the MDA). The Accounts table has been added to the site map (a new active unmanaged later on the site map).


**Step 3 – Back in the Dev environment**

The Created By column has been added to the Weather Log form, and the Address Dataverse table has been added as a page to the site map, resulting in a new unmanaged version to be deployed to QA again.


## The Interesting Bit

I have purposely started a new section after the second deployment, and I promise I am not deviating 😉.

In my first blog post, when I deployed the updated Canvas app to QA, because the managed Canvas app in QA had active unmanaged layers, the updates did not take effect. The active unmanaged layers first had to be removed, resulting in all that work being lost. Only then could I deploy and see the updates take effect.

In this scenario, objects like site maps and forms work differently. Despite having active unmanaged layers on both the Model-Driven app and the site map, the updates from the second deployment have taken effect. More so, the changes from dev and the updates in the unmanaged layer both show up in the Model-Driven app and site map. Wild right? It’s as if the changes and the layers have been merged. But if I relook at both my MDA and site map objects, I can still clearly see the active unmanaged layer.


## A Mystery Unveiled

So I now have two sets of changes working in unison. But what happens if I delete the unmanaged layers? In the above steps, I included a screenshot of the MDA and site map unmanaged layers. But if you give it some thought, a form is not built in a Model-Driven app, it’s built on the table directly. If I look at the layers for the Weather Log table in my QA environment, despite updating the form, there is no active unmanaged layer.


I then went and deleted the unmanaged layers for the MDA and the site map. The site map and MDA pages reverted to what the solution from my Dev environment deployed, but for some reason, the form still had the Status and Status Reason columns in it. Didn’t I just remove all the unmanaged layers? Didn’t I just check to see if there was an unmanaged layer on the Weather Log table?


I am 100% right in knowing there should be an active unmanaged layer for the form on the Weather Log table, but for some peculiar reason, you cannot see this layer in the default Power Platform solution view. If I switch my solution back to the classic editor and select Entities > Weather Log > Forms, I’ll be able to see the forms as objects in my solution. If I then select the form I updated directly in QA and then click solution layers, voila 🎉. I can now see the active unmanaged layer on the form I updated.


I’ve now removed the unmanaged layer and republished the solution in QA, and as expected, I can now only see the updates deployed from Dev to QA and no longer have any unmanaged layers in my solution.


## Conclusion

Solution layers can be tricky buggers at times. It’s imperative, as a Power Platform developer, that we become familiar with the classic functionality as well. There have been so many things I personally have learned after trying to figure out how I can achieve something through the new UI, but I never considered going through the classic editor.

On a separate note, this post brings my ALM series to a final close. ALM is a passion that came about from simply trying to understand basic ALM frameworks and concepts. Blogging about ALM has not just allowed me to branch further into the community but has also been a tremendous learning curve for me, and it’s something I will continue to grow with as my career progresses. I definitely plan on touching base with some more ALM content in the near future, but for now, it’s time to end this chapter. (P.S. This is not the end of my blogging, there’s plenty more to come 😉)