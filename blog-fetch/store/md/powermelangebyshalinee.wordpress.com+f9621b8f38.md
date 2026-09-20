**Problem Scenario 1:** There might be a situation where you deleted a list of data but due to some reason you want it back. We can get this list from the last backup taken. But then these records would need to be created again with the same guids. How can we do it ?

**Solution**: We can read the guids from the list and pass it here:

In the “Add a New row” step, expand the “Show Advanced Options”

& then fill in the unique identifier. This way you can create records with given guids.

While writing about it, another problem came to my mind, where what if i wanted to create a lead without filling in the Topic which is a mandatory field as because in the normal way, it throws an error if you do not write something.

**Problem Scenario 2:**We do have a scenario where we have to bulk data upload where we have to override the required fields. Here can be a Power Automate Solution to it where it can be put as a conditional check.

Well, some good Eidetic memory skills came in handy here. I remembered that Update Action does not require any field specifications. thus i got the idea to generate a random guid and pass it on.

**Solution:** Create a Compose action where you write the expression “guid()” – this basically creates a random guid for you & then use this guid in the update a row step. This basically acts like “UPSERT” where we do not have to fill in all the mandatory fields.

Woohoo! it works.

You can see the lead being generated here without the Topic & Last Name:

Also tried putting null in “add a new row” step.

Surprisingly it works- that was quite simple!

Find the lead generated here:

Hope you got some great tips today on how to create guids using the guids() expression? What can be the use cases?

& the ***Power Quote*** of the day is:

“Mastering others is strength. Mastering yourself is true power.”