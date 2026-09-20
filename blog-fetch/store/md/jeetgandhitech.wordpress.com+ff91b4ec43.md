FetchXML is a proprietary query language used in Dataverse to retrieve data. It’s XML-based and supports advanced operations like joins, filtering, aggregation, and ordering.

### **FetchXML Basic Structure**

```
<fetch version="1.0" output-format="xml-platform" mapping="logical" distinct="false">
  <entity name="account">
    <attribute name="name" />
    <attribute name="accountid" />
  </entity>
</fetch>
```
### Advanced Scenarios

- **Filtering with Multiple Conditions**  - You can use with and / or operators:

```
<entity name="account">
<attribute name="name" />
<attribute name="accountid" />
<filter type="and">
  <condition attribute="statecode" operator="eq" value="0" />
  <condition attribute="revenue" operator="gt" value="1000000" />
</filter>
</entity>
```
- **Linked Entities (Joins)**  - Join related tables using :
    - link-type: inner or outer
    - alias: Used for referring to joined columns
- Join related tables using :

```
<entity name="contact">
  <attribute name="fullname" />
  <link-entity name="account" from="accountid" to="parentcustomerid" link-type="inner" alias="acc">
    <attribute name="name" />
  </link-entity>
</entity>
```
- **Aggregation and Grouping**  - To perform aggregate operations:
    - aggregate=”true” enables aggregation
    - Use sum, avg, count, min, max
- To perform aggregate operations:

```
<fetch mapping="logical" aggregate="true">
  <entity name="opportunity">
    <attribute name="estimatedvalue" alias="totalrevenue" aggregate="sum" />
    <attribute name="customerid" alias="customer" groupby="true" />
  </entity>
</fetch>
```
- **Using Aliases**  - Refer to fields from linked entities or aggregated fields:

```
<attribute name="revenue" alias="totalrevenue" aggregate="sum" />
```
- **Date Filters**  - Fetch records from the last 30 days:
  - Other date operators: today, yesterday, next-x-weeks, etc.

```
<condition attribute="createdon" operator="last-x-days" value="30" />
```
- **Top N Records**

```
<fetch top="5">
  <entity name="lead">
    <attribute name="fullname" />
    <order attribute="createdon" descending="true" />
  </entity>
</fetch>
```
### **Execution Options**

- **Power Automate (List Rows with FetchXML)**  - Use List Rows in the Dataverse connector
  - Paste FetchXML in the “Fetch XML Query” field
- **Plugin or Custom Workflow**  - Use FetchExpression or QueryExpression in C# plugins:

```
var fetchXml = "your FetchXML string here";
EntityCollection result = service.RetrieveMultiple(new FetchExpression(fetchXml));
```
- **XrmToolBox – FetchXML Builder**  - Great tool for building and testing FetchXML
  - Auto-generates queries and lets you preview results
  - **Highly Recommended for building complex FetchXML queries**

### **Tips and Best Practices**

- Always use alias for disambiguation in joins or aggregation
- Avoid unnecessary link-entity if not retrieving related fields
- Use filters efficiently to reduce query load
- Test performance impact of aggregate queries

## Leave a comment