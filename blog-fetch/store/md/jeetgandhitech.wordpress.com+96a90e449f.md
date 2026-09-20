## (Client-Side) Bulk Operations Using JavaScript

JavaScript is primarily used for form-level or ribbon-based operations in Dynamics 365. While client-side operations can handle small data operations, bulk processing should be handled **carefully to avoid performance issues**.

### Best Practices

- **Use Batch Requests with Web API**

When executing multiple operations, use batch requests. They help reduce the number of API calls and optimize performance. Batch requests allow you to combine multiple create, update, and delete operations into a single HTTP request.

Example: Batch Create using JavaScript

```
const webAPIUrl = Xrm.Utility.getGlobalContext().getClientUrl() + "/api/data/v9.2/$batch";
const requestBody = `
--batch_123
Content-Type: application/http
Content-Transfer-Encoding: binary
POST /api/data/v9.2/accounts HTTP/1.1
Content-Type: application/json
{"name": "Account A", "accountnumber": "12345"}
--batch_123
Content-Type: application/http
Content-Transfer-Encoding: binary
POST /api/data/v9.2/accounts HTTP/1.1
Content-Type: application/json
{"name": "Account B", "accountnumber": "67890"}
--batch_123--`;
const req = new XMLHttpRequest();
req.open("POST", webAPIUrl, true);
req.setRequestHeader("Content-Type", "multipart/mixed;boundary=batch_123");
req.onreadystatechange = function () {
    if (req.readyState === 4 && req.status === 200) {
        console.log("Batch request successful");
    }
};
req.send(requestBody);
```
- **Use Asynchronous Execution**  - Perform bulk operations asynchronously using Promise or async/await to prevent UI blocking.
  - This ensures a better user experience and reduces the interface’s freezing risk.

- **Chunk Large Operations**  - For bulk operations exceeding 1000 records, chunk the data into smaller batches (e.g., 200-500 records).
  - This prevents timeouts and improves the execution success rate.
- **Optimize Data Retrieval**  - Use OData $select and $filter clauses to retrieve only the necessary fields.
  - Avoid fetching unnecessary columns, as it slows down performance.

```
const query = "/api/data/v9.2/accounts?$select=name,accountnumber&$top=50";
```
- **Use Parallel Execution Cautiously**  - In scenarios where you can run operations in parallel, use Promise.all() but limit the concurrent requests to avoid throttling.

## (Server-Side) Bulk Operations Using C#

For bulk operations, C# offers better performance as it runs server-side and handles large datasets efficiently.

### Best Practices

- **Use ExecuteMultipleRequest for Bulk Operations**

The ExecuteMultipleRequest allows you to perform bulk create, update, or delete operations in a single API call. It reduces the round trips to the server, improving efficiency.

Example: ExecuteMultipleRequest

```
using Microsoft.Xrm.Sdk;
using Microsoft.Xrm.Sdk.Messages;
using Microsoft.Xrm.Sdk.Client;
using System;
using System.Collections.Generic;
public void BulkUpdate(IOrganizationService service, List<Entity> entities)
{
    ExecuteMultipleRequest multiReq = new ExecuteMultipleRequest
    {
        Requests = new OrganizationRequestCollection(),
        Settings = new ExecuteMultipleSettings
        {
            ContinueOnError = true,
            ReturnResponses = true
        }
    };
    foreach (var entity in entities)
    {
        UpdateRequest updateRequest = new UpdateRequest { Target = entity };
        multiReq.Requests.Add(updateRequest);
    }
    ExecuteMultipleResponse response = (ExecuteMultipleResponse)service.Execute(multiReq);
    Console.WriteLine($"Success: {response.Responses.Count(r => r.Fault == null)}");
}
```
- **Use Multi-threading for Large Datasets**  - For large operations, use Parallel.ForEach() or Task.Run() to execute batches concurrently.
  - This speeds up execution but must be controlled carefully to avoid overloading the server.
- **Use FetchXML with Paging for Large Data Sets**

Use paging when retrieving large datasets to avoid timeouts and memory overflows.

Example: FetchXML with Paging

```
string fetchXml = @"<fetch mapping='logical' count='5000' page='{0}'>
                      <entity name='account'>
                        <attribute name='name' />
                      </entity>
                    </fetch>";
int pageNumber = 1;
EntityCollection result;
do
{
    string xml = string.Format(fetchXml, pageNumber);
    result = service.RetrieveMultiple(new FetchExpression(xml));
    
    // Process records here
    foreach (var entity in result.Entities)
    {
        Console.WriteLine(entity["name"]);
    }
    pageNumber++;
} while (result.MoreRecords);
```
- **Minimize SDK Calls**  - Reduce the number of SDK calls by batching operations.
  - Use ExecuteMultiple and UpsertRequest instead of multiple Create or Update calls.
- **Handle Exceptions Gracefully**  - Implement exception handling for partial success and fault tolerance.
  - Use ContinueOnError in ExecuteMultipleRequest to prevent the entire batch from failing due to a single record.

## Key Differences Between JS and C# for Bulk Operations

| **Aspect** | **JS(Client-Side)** | **C#(Client-Side)** | 
| Execution Location | Runs on the client/browser | Runs on the server | 
| Performance | Suitable for smaller operations (100-200 records) | Better for large operations(>1000) | 
| API Efficiency | Requires batch requests to optimize | ExecuteMultiple improves efficiency | 
| Data Volume | Limited by client-side resources | Can handle large datasets | 
| Error Handling | Less effective error handling | Robust exception handling | 

## Recommendations

- For large-scale operations: Use C# server-side logic with ExecuteMultipleRequest.
- For small-scale bulk operations: Use JavaScript with batch requests.
- For massive datasets: Implement multi-threading with C# and batch execution for optimal performance.
- Use FetchXML with paging: To avoid timeouts and retrieve large datasets efficiently.

## Leave a comment