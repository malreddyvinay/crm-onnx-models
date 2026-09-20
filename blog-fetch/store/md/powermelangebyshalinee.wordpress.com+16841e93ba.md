Integrating Dynamics 365 with Azure Data Lake allows you to continuously sync operational data for cost-effective big data analytics, AI workloads, and custom reporting.

The datatypes handshaked between Datalake to Dataverse is explained below:

| **DataType in Dataverse** | **DataType in Datalake** | 
| Text | Varchar | 
| Number | Decimal/Integer as needed | 
| Date | Date | 
| Lookup | Guid | 
| Choice | Integer Value of option set | 
| Boolean | true/false | 

Thus to send any lookup values, you need to store the masters in a table in Datalake and send the respective guids instead of the value. Eg; City master. Also when you take back data from Dataverse to Datalake, you would get the unique guid only and not the value itself.

To know more in detail, here is the link. Here customizing the batch size is explained in detail too, do have a read.

**Power Tip**: To avoid backtracking again, you can create Power Fx columns in dataverse to store the text values and take them directly for values.

**Please Note**: The Dynamics data types  **AttributeType.CalendarRules**, **AttributeType.MultiSelectPicklist**, and **AttributeType.PartyList** aren’t supported.

While fetching data from the entire entity using the Synapse pipeline sometimes the execution intermittently fails with various errors.

**Problem Statement**: One such scenario we faced was that some columns were missing when we imported the schema or preview data even though the attributes were present on the FetchXML.

**Cause**: On inspection, we found that this issue is by design, because Data Factory and Synapse pipelines are unable to show columns that contain no values in the first 10 records.

**Solution**: Explicit Mapping is what we need here-  firstly map the columns which you need

While configuring Explicit Mapping, we manually added the mapping for the missing columns along with their corresponding data types into the JSON definition of the Copy activity. This helped resolve the issue, and the data was successfully fetched without missing the column.

Once you have done it, you will be able to see all the required columns in your target entity.


For more errors, you can read here.

**Discussion**: The intermittent nature of the issue is primarily influenced by resource availability within the Dataverse execution engine. When sufficient resources are available, the query can be processed successfully and the results are returned as expected. However, during periods of higher load or resource constraints, the same query may fail due to the increased processing requirements associated with the complex entity structure.

The observed error refers to the following document: Query anti-patterns (Microsoft Dataverse) – Power Apps | Microsoft Learn

The guidance in the document suggests 

1. Minimizing the number of selected columns to improve query performance.

2. Minimize the number of selected logical columns

3.Avoid leading wild cards in filter conditions

4.Avoid using formula or calculated columns in filter conditions

5.Avoid ordering by choice columns

6.Avoid ordering by columns in related tables

7.Avoid using conditions on large text columns

In our case,

- It was identified that the issue is related to the presence of multiple complex data types within the entity being queried.
- Several of the columns contain reference values and relationships to other entities. As a result, the overall query response becomes significantly larger and more resource-intensive to process.
- Due to the complexity and size of the generated result set, the query may fail under certain conditions with the observed error.

Additionally, this behavior is not specific to Azure Data Factory. Any client or tool attempting to retrieve the same dataset using a similar query pattern may encounter the same issue because the limitation originates from the query execution and result generation process within Dataverse.

**Another Use Case**: For large organizations , managing and analyzing large volumes of audit data can become increasingly complex and costly. We can export Audit Log from Dataverse for compliance and governance. It is explained here.

Now, Azure Synapse Link allows direct sync with Azure Synapse Analytics.

Happy Reporting!

Hoping the above explanation helps you if you are trying to import/export from Datalake.

& the **Power Quote** of the Day is:

*“Sometimes the strongest thing you can do is begin again, wiser than before. The power of **Restart** lies in believing that your next chapter can be better than the last.”*