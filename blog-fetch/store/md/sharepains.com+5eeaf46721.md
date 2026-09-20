Filter queries are important when you work with SharePoint Get Items actions or Dataverse Get Rows, but how about the Excel Filter Query setting?

## Get rows present in a Table

The Get rows present in Table also has the Excel Filter Query setting. In the above mentioned posts I’ve gone through all the options available to SharePoint and Dataverse. Even though Excel is not the best database option. A lot of people use Excel to import data using Power Automate.

Excel or csv files is such a common way of exporting data, when APIs aren’t available, that it is worth considering Excel at least for data import purposes. Excel is definitely not a good data source to run as a database for your app in Power Apps.

The first step is the add the List rows present in a table action to your flow and then one of the settings is the Filter Query setting as shown below.

In the above action settings you will recognise a similar syntax to my previous posts about query filters.

## Basic Excel Filter Query

The basic excel query filter will follow the following format:

`Column eq 'value'`
To identify the Column name you could simply look at the Excel file and copy the column name, but …

## Column names in Excel

Imagine the following Excel spreadsheet:

And when I get flow to return the data, I may get something like this:

```
[
    {
      "@odata.etag": "",
      "ItemInternalId": "702c19df-9858-4d38-9561-a577fd87a864",
      "Title": "Date 2",
      "Date": "44229",
      "Another Column": "More data",
      "Some Weird & Wonderful Characters!": "Some information",
      "Number": "2"
    }
  ]
```
At a first glance this might just look like normal data. But there are a couple of potential problems here.

Dates in Excel formats appear as numbers.

Once setting The DateTime Format to ISO 8601, the date will come back in a understandable format

```
  {
      "@odata.etag": "",
      "ItemInternalId": "e5e77485-3c2b-44bb-8970-85d0ceeb44a4",
      "Title": "Date 2",
      "Date": "2021-02-02T00:00:00.000Z",
      "Another Column": "More data",
      "Some Weird & Wonderful Characters!": "Some information",
      "Number": "2"
    }
```
The other issue here is that the number appears as text. Will this mean that we can’t treat this as a number? Also how about those spaces and troublesome character like & and !

## Handling column names

If we were to use the following expression in the Excel Query Filter we will get an error message

`Another Column eq 'Mode data`
So even though we used the fieldname the query filter will not be able to handle the space in the column name as the following error is thrown:

Syntax error at position 14 in ‘Another Column eq ‘Mode data”.\r\n inner exception: Syntax error at position 14 in ‘Another Column eq ‘Mode data”

Other connectors may support syntax like _x0020_ to replace spaces or square brackets [] around the field name, the the Excel Filter Query doesn’t support this. So this may mean that you have to remove the spaces from your columns. Or alternatively you could use the Filter Array action to do the filtering. But that would be less efficient, especially for larger Excel files.

## Excel Query Filter functions

The Excel Filter Query, unlike the Dataverse and SharePoint equivalent supports a very limited amount of queries.

The operations currently supported are

- eq
- ne
- contains
- startswith
- endwith

If you use any other options you will get the following error:

*Only single ‘eq’, ‘ne’, ‘contains’, ‘startswith’ or ‘endswith’ is currently supported.*

This does mean that we cannot filter multiple columns at the same time. So if you wanted to filter by multiple columns, you could either concatenate columns together in your Excel spreadsheet or you may have to use the earlier mentioned Filter Array action.

## Eq

The Eq operator is to select records where a column matches a certain value

`columnname eq 'text value'`
Notice that you will need single quotes around the value and no quotes around the column name. Aa as mentioned before the column name can’t include special characters or spaces.

## Ne

The Eq operator is to select records where a column does not match a certain value

`columnname ne 'text value'`
## Contains

The Contains function is to select records that contain a specified text value

`Contains(columnname, 'text')`
## Startswith

The Startswith function is to select records that start with a specified text value

`Startswith(columnname, 'text')`
## Endswith

The Endswith function is to select records that end with a specified text value

`Endswith(columnname, 'text')`
## Further thoughts on Excel Query Filter

As we can see from the available operations and functions Excel is limited in its query options. Hence the “Excel is not a database” comment read on many forums when people have problems with handling Excel files. So please avoid Excel where you can.

### FAQs

## Excel Query Filters are quite limited. Are there alternatives?

When using Excel as a datasource, the limitations can be a problem. When there are high volumes of data alternatives may need to be considered.

The following options are alternatives:

- SharePoint (For lower volumes of data)
- Dataverse (For higher volumes of data)
- SQL Server (For high volumes of data that require very high performance)

### Discover more from SharePains

Subscribe to get the latest posts sent to your email.

Thanks for this. I currently have a scenario where I have to apply a filter query on the list rows action, but my column has space between and I can’t currently filter. I think its something MS really have to work on. I can’t just join the column name in Excel because the scenario is not ideal

The easiest way to handle that will be to get all the content from the table and then use the filter array to select the data. It would be better to do that with filter queries as you wouldn’t be collecting all the data first. How many rows does your Excel table have?

Hi Peter,

I need to send an email to the Employee whose Employee Status is active in my excel.

If I insert the filter query( Employee Status eq ‘Active’) in the List row present in a Table function. Getting below error

(Syntax error at position 15 in ‘Employee Status eq ‘Active”. inner exception: Syntax error at position 15 in ‘Employee Status eq ‘Active”.)

Would you kindly assist me in debugging this error?

Hi Rohit, the space in your column name is causing the issue.

Thank you, Pieter, for pointing out my mistake. I apologize for bothering you with this minor issue had I read your post more carefully, I could have resolved it myself. I tried other methods, but they didn’t work. After removing the issue, everything is working fine now.

Superb! Another very well explained article. Thank you. Made me find out my issue with the Column Name having spaces.