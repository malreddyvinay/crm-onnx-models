Creating date and time columns (aka fields) in Microsoft Dataverse is a really straightforward process, however, you really should take a pause to make sure you are configuring the right *type* of date and time column.

Check out the companion video for this post, where not only will you learn about date and time columns, but also some fun facts about Sir Sandford Fleming.

When creating Date and time columns in Dataverse, you have different options:

- Date only
- Date and Time

And then you need to decide if you want user local or time zone independent

When you run your app (in this case, a model driven app) At first glance, the fields with date and time look the same.

However, users might be living and working in different time zones, and will set their personal preferences appropriately.

We’ll then see the difference, even though we did not change the data itself.

If we were to look on a Power Pages website, the times would reflect the time zone settings of the device the web page is being viewed on.

## What are some good use cases for user local date time fields?

- Scheduling international conference calls or webinars.
- Financial market trading times across different stock exchanges.

(Note – earlier I had some other examples, but some people with the initials “G.D.” made some arguments of why these should be time zone independent date time fields)

## What are some good use cases for time zone independent date time fields?

- Store opening and closing times
- Birthdays
- Legal documents
- Airline arrival and departure times

As always… “It depends” ©️

## Summary

Small things can cause huge impacts. Making a configuration on a date time column early in a process could have big impacts later after a big data migration and go-live. (Again, apologies to those folks in Vancouver who showed up at 6am for a class that was scheduled by a user in Ontario that was really supposed to start at 9am… oops!)

Going to MVP Summit? Consider coming to the Canadian Power Platform Summit in Vancouver, March 15th and 16th.

Cover photo by Windows on Unsplash

*Nick Doelman is an independent Power Platform trainer and coach, presenter, Microsoft Certified Trainer, competitive Powerlifter, , former Microsoft employee, once again: Microsoft MVP, and cohost of the Power Platform BOOST! podcast.*

## One thought on “Date and time columns in Dataverse”