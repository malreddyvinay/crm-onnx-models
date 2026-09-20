Every now and then, you may need a plugin to run for any entity, but, when registering a plugin step using the plugin registration tool, you may notice that you are unable to filter such steps by attribute since that option is simply disabled:

Which makes sense, since, for the most part, columns are table-specific, so, when running some code on any table, you can’t expect the same columns all the time.

And, yet, some columns will be present in more than one table. Such as *ownerid*, for example. But, also, you can even make it part of your “database design” and ensure that a column with some “standard” name has been added to all the tables you want the plugin to run for. In which case you may want to take advantage of having just one plugin execution step in your solution (vs having multiple steps, one per table).

So, to work around that limitation of the plugin registration tool, do this:

- Start adding a step
- Specify the message (“Update”, but can also use “Create”)
- Choose a table that has the column you are interested in as if you were setting up that step for a specific table
- Configure “filtering by attributes”
- Then clear up “Primary Entity” field to make it work for “any” entity

“Filtering by attribute” will stay configured: