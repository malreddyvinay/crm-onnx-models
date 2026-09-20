#### Some details in the **Power Platform** are intentionally ***excluded*** from the solutions. Still, most of us developers think they ***are*** part of them—unless we read enough about the docs (which is boooring).

One example is **Seed** for columns that have the type **Autonumber**.

**excluded**

**are**

As far as I know, the **seed** is not stored in our tables or columns; it is only known in the deep down of the mystery **SQL Server**. So, how can it even be settable in the **Maker Portal**?

We have to be able to set “*what should be the next number value*” in some way by those auto number columns.

Of course, it is very nice that we ***can*** set the seed. However, the seed is not included in the solution, so we can’t “*build and deploy*” and make sure we have the same number sequence in the TEST and PROD environments. How do we handle this when we want to be our good guys and gals and stay with a **Healthy ALM** structure?

We have to fake it a bit…


When we live in a **Healthy ALM** world, having **managed solutions** *(read: **Case Closed** from 2018, unfortunately still relevant)* everywhere, except in the **DEV** environment, and we need to update the seed, how do we change it in the solutions since, well, you know, it’s **managed**?

A seed is just a seed, then the seed grows up…


Another issue is that we can only see the original seed, which by default is **1000**. If we have created **50** records, the next record will get number **1051**. But we can’t see it here since a “seed” only shows how it will start, and it is never possible to find what the next value will be.

## Changing the Seed

Instead, we go to the **Default solution** and find the table (of millions…), and we find the column where we have the `Autonumber` format.

*I curse myself when I do that, but I do it anyway…*

**Now, we can set the seed!**

Doing that makes the platform set a layer above the managed solution, an unmanaged layer… ???? That works against the ***Healthy ALM*** and my gut feeling and my brain hurts, and it’s hard to sleep tonight.

But nothing was ***really*** changed! We only set the seed, but when we save the whole column, it can’t differ from what was actually changed, so we get the new layer.

When we now know that this “unmanaged change” is not a change. Therefore, we can now undo the unmanaged layer.

It works, but it’s a bit of an unnecessary detour.

## There’s a better way…

Setting the Seed is technically not done by updating the column. Instead, there is a specific request in the API called **SetAutoNumberSeedRequest*****not*** change or touch the column.

You can create your code to execute that request. Or just use what is already available.

I like code, but I assume most people don’t.

That’s why I create tools. No-code tools.


This feature is used in the **Auto Number Manager** tool in **XrmToolBox**.

As you can see in this short video, you select the table (entity) and the column (attribute). Then, we can let it guess what its current value is, this is not affecting anything, but might be good to see how far from the original seed we are.

Then we enter the value for the new seed, sort of to restart from that initial value.

When we click the **Update** button, it checks to see if anything has been changed in the column; if not, it won’t be saved. This means that there will not be an unmanaged layer (unless you change some parts of the auto number column).

After triple-checking the layers, I realized that using this feature in **Auto Number Manager** will still keep the column in a **managed layer**, and now your ***Healthy ALM*** will secure your system.

This tool was created in 2017 after attending **eXtreme365** in Lisbon, Portugal. **MattB** at **Microsoft** told us that this new request was added to the SDK, but nothing has been added to the UI yet. A few years ago, the **Autonumber** was added to the **Maker Portal**, making my tool obsolete. I notice from my stats that the tool is still used ~50 times a day anyway. On the first of January, it is used hundreds of times every year.

After my customer made this request, I realized that my tool is still needed—in this case, to **set the seed**.