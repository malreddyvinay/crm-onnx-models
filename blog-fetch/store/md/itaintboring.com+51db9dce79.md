What exactly is the difference between solution upgrade and solution update?

It might not be quite obvious from the description of each operation when you are importing a solution:

Let’s do a quick test then. To start with, here is how my original solution looks like – there is nothing fancy there, it’s just a couple of tables:

Normally, one of the main benefits of using managed solutions is considered to be our ability to delete no longer needed components from the destination environment. Those components that are removed from the newer version of the solution, and which have no other references holding them, are expected to be removed from the destination during the upgrade operation.

And that is how it works, but only for solution “upgrades”.

Instead of the upgrade, I’m going to use “Update” this time. Here is how my new solution looks like in the source:

There is one new table, but, also, one of the older tables has been removed.

Once this solution is imported into the destination with “Update” option, here is what it looks like in the destination:

It seems this is not so much about replacing the solution as it is about adding what’s been added without removing what’s been removed.

That, of course, goes against the ALM ideas, so why would somebody want to do this? In my case, I somehow ran into an endless loop of missing dependencies when trying to do the upgrade, and, eventually, had to resort to the update option just to get the solution pushed to the destination environment.

That means, though, that some of the components which would normally be deleted are still there, and that is not good either. But that is a problem for another day, which, of course, I still have to look into.

Hi Alex. Very insightful way of explaining Upgrading a solution vs updating a solution as the MSFT doc doesn’t make this quite as clear. Effectively Update is augmenting the solution.