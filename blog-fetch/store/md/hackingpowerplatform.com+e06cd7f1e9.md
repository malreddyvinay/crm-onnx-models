UPDATE: Microsoft has released documentation describing these features. All features mentioned in this article are now fully supported.

## Introduction

When using the Dataverse web api, you can do more advanced queries with OData than you can with FetchXml/QueryExpression. First, let’s talk a little about operations that OData can do, which FetchXml cannot.

## The dataset

Let’s say we have two contacts in our Dataverse environment:

Contact 1:

- Fullname: Contact without any Tasks
- Tasks: None

Contact 2:

- Fullname: Contact with Tasks
- Tasks (2):
- Task 1:
  - Subject: Please make me coffee
  - Status: Closed (1)
- Task 2:
  - Subject: Please approve my holiday
  - Status: Active (0)

## About OData vs FetchXml

Now, let’s say that we want to get the contacts where ALL of the Tasks are Active (eq 0). We can do that with the following OData filter:*[DataverseOrgUrl]/api/data/v9.2/contacts?$filter=Contact_Tasks/all(t:t/statecode eq 0)*Result:

[None] (The ‘Please make me coffee’ task is Closed)

There is no (official) equivalent FetchXml query for this. When querying related tables with FetchXml, you can do the following things:

- Get all rows that do NOT have any rows associated to them at all (not-in)
- Get all rows that have ANY rows associated to them
- Get all rows where ANY of the related rows satisfy a given condition

With OData, we can the above, and much more:

- Get all rows where ALL of the related rows satisfy a given condition
- Get all rows that do NOT have ANY rows that satisfy a given condition
- The given condition can also be a similar ANY/ALL query to a related (nested) table.
- The filters on related tables can all be grouped in AND/OR clauses, allowing for very complex filters.

**Some more examples**:

Get all contacts where ALL tasks are Active (eq 0), or ANY task is Closed (eq 1) AND has the Subject ‘Please make me coffee’:*[DataverseOrgUrl]/api/data/v9.2/contacts?$filter=Contact_Tasks/all(t:t/statecode eq 0) or Contact_Tasks/any(t:t/statecode eq 1 and t/subject eq ‘Please make me coffee’)*Result:

[Contact with Tasks]

Get all contacts that do NOT have any Tasks, or all Tasks are Closed (eq 1):*[DataverseOrgUrl]/api/data/v9.2/contacts?$filter=not Contact_Tasks/any() or Contact_Tasks/all(t:t/statecode eq 1)*Result:

[Contact without any Tasks]

## How to do more advanced queries with FetchXml

It turns out that all of the above queries are possible to do with FetchXml, using undocumented operators. Let’s go back to the first example: Get contacts where ALL of the Tasks are Active. For simplicity, let’s only select the attribute ‘fullname’.

First the OData fetch:*[DataverseOrgUrl]/api/data/v9.2/contacts?$filter=Contact_Tasks/all(t:t/statecode eq 0)&$select=fullname*

You can do this with the following FetchXml:

```
<fetch distinct="false" useraworderby="true" no-lock="false" mapping="logical">
	<entity name="contact">
		<attribute name="fullname"/>
		<filter type="and">
			<filter type="and">
				<link-entity name="task" to="contactid" from="regardingobjectid" link-type="all">
					<filter type="and" anyallalias="task1">
						<condition attribute="statecode" operator="ne" value="0"/>
					</filter>
				</link-entity>
			</filter>
		</filter>
	</entity>
</fetch>
```

 

What’s happening here? Two nested filter elements, followed by a link-entity with link-type=”all”. It turns out that using this syntax, you can create the equivalent of the more complex OData queries! If you look closely, you can see that the statecode value filter is ‘ne 0’ instead of ‘eq 0’. Why is that? It turns out that Dataverse inverts all conditions in the query when link-type=”all”

Let’s go to the second exemple: Get all contacts where ALL tasks are Active (eq 0), or ANY task is Closed (eq 1) and has the Subject ‘Please make me coffee’. Only select the fullname. OData query:*[DataverseOrgUrl]/api/data/v9.2/contacts?$filter=Contact_Tasks/all(t:t/statecode eq 0) or Contact_Tasks/any(t:t/statecode eq 1 and t/subject eq ‘Please make me coffee’)&$select=fullname*

This corresponds with the following FetchXml:

```
<fetch distinct="false" useraworderby="true" no-lock="false" mapping="logical">
	<entity name="contact">
		<attribute name="fullname"/>
		<filter type="or">
			<filter type="and">
				<link-entity name="task" to="contactid" from="regardingobjectid" link-type="all">
					<filter type="and" anyallalias="task1">
						<condition attribute="statecode" operator="ne" value="0"/>
					</filter>
				</link-entity>
			</filter>
			<filter type="and">
				<link-entity name="task" to="contactid" from="regardingobjectid" link-type="any">
					<filter type="and" anyallalias="task1">
						<condition attribute="statecode" operator="eq" value="1"/>
						<condition attribute="subject" operator="eq" value="Please make me coffee"/>
					</filter>
				</link-entity>
			</filter>
		</filter>
	</entity>
</fetch
```
 

Again, the conditions in the link-type=”all” link-entity seem to be inverted. For the link-type=”any” link-entity, this is not the case.

And the third OData example: Get all contacts that do NOT have any Tasks, or all Tasks are Closed (eq 1). Select the fullname. OData query:*[DataverseOrgUrl]/api/data/v9.2/contacts?$filter=not Contact_Tasks/any() or Contact_Tasks/all(t:t/statecode eq 1)*

FetchXml:

```
<fetch distinct="false" useraworderby="true" no-lock="false" mapping="logical">
	<entity name="contact">
		<attribute name="fullname"/>
		<filter type="or">
			<filter type="and">
				<link-entity name="task" to="contactid" from="regardingobjectid" link-type="not any">
					<filter type="and" anyallalias="task1"/>
				</link-entity>
			</filter>
			<filter type="and">
				<link-entity name="task" to="contactid" from="regardingobjectid" link-type="all">
					<filter type="and" anyallalias="task1">
						<condition attribute="statecode" operator="ne" value="1"/>
					</filter>
				</link-entity>
			</filter>
		</filter>
	</entity>
</fetch>
```

 

Let’s make a filter with more nested tables and see what the resulting FetchXml is. This filter retrieves all contacts where NOT ALL of the cases (incident) have ANY tasks. Select the fullname. OData query:*[DataverseOrgUrl]/api/data/v9.2/contacts?$filter=not incident_customer_contacts/all(c:c/Incident_Tasks/any())&$select=fullname*

FetchXml:

```
<fetch distinct="false" useraworderby="true" no-lock="false" mapping="logical">
	<entity name="contact">
		<attribute name="fullname"/>
		<filter type="and">
			<filter type="and">
				<link-entity name="incident" to="contactid" from="customerid" link-type="not all">
					<filter type="and" anyallalias="incident1">
						<filter type="and" anyallalias="incident1">
							<link-entity name="task" to="incidentid" from="regardingobjectid" link-type="not any">
								<filter type="and" anyallalias="task1"/>
							</link-entity>
						</filter>
					</filter>
				</link-entity>
			</filter>
		</filter>
	</entity>
</fetch>
```
 

Note that all of the conditions under the ‘not-all’ are inverted, even the link-entity (‘not any’ vs ‘any’).

So how did I work this out? I did not write these fetches by hand. It was simple: just create a PreOperation plugin that runs on the RetrieveMultiple of a given table. Write the Query from the context InputParameters to the trace log. Then do OData queries and see what the resulting FetchXml is. This is the code for the plugin:

```
using Microsoft.Crm.Sdk.Messages;
using Microsoft.Xrm.Sdk;
using Microsoft.Xrm.Sdk.Query;
using System;
namespace TestPlugin
{
    public class LogQueryPlugin : IPlugin
    {
        public void Execute(IServiceProvider serviceProvider)
        {
            var context = serviceProvider.GetService(typeof(IExecutionContext)) as IExecutionContext;
            var tracer = serviceProvider.GetService(typeof(ITracingService)) as ITracingService;
            var orgServiceFactory = serviceProvider.GetService(typeof(IOrganizationServiceFactory)) as IOrganizationServiceFactory;
            var organizationService = orgServiceFactory.CreateOrganizationService(context.UserId);
            var query = context.InputParameters["Query"] as QueryBase;
            if (query is FetchExpression fetch)
            {
                tracer.Trace(fetch.Query);
            }
            else if (query is QueryExpression qe)
            {
                var qeToFetchRes = organizationService.Execute(new QueryExpressionToFetchXmlRequest { Query = qe }) as QueryExpressionToFetchXmlResponse;
                tracer.Trace(qeToFetchRes.FetchXml);
            }
        }
    }
}
```
## Using the FetchXml in views.

I haven’t tried to use these fetches in System Views, but it might just work. I you are interested, give it a try and let me know the results. I will update the blog post.

## Supported?

Using undocumented features is mostly not supported by Microsoft. However, I don’t think that features that are part of the ‘core’ system such as FetchXml queries are prone to breaking changes. It’s probably safe to use this in production. But use at your own risk.