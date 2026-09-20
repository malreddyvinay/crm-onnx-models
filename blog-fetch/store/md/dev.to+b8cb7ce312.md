If you’ve worked with **Xrm.WebApi** in Dynamics 365, you know it’s a powerful tool for interacting with the Web API from JavaScript. In my previous post Web API vs XMLHttpRequest in Dynamics 365: Which One to Use?, I compared `Xrm.WebApi` to `XMLHttpRequest`. Now, let’s dive deeper into `Xrm.WebApi` itself—specifically, the difference between **synchronous** and **asynchronous** calls.

Understanding when and how to use these approaches can make your code more efficient and user-friendly. Let’s break it down with examples and best practices.

## Xrm.WebApi: A Quick Recap

`Xrm.WebApi` is Microsoft’s native JavaScript API for Dynamics 365, designed to simplify Web API interactions within forms, web resources, and client-side scripts. It supports common CRUD operations (create, retrieve, update, delete) and offers two execution modes:

- 
**Asynchronous** : Uses promises for non-blocking calls (default behavior).
- 
**Synchronous** : Blocks execution until the operation completes (optional, with some setup).

But which one should you use? Let’s explore both.

## Asynchronous Xrm.WebApi Calls

By default, `Xrm.WebApi` methods like `retrieveRecord`, `createRecord`, `updateRecord`, and `deleteRecord` are asynchronous. They return promises, allowing your code to continue running while the server processes the request.

### Why Use Asynchronous Calls?

- 
**Better User Experience** : Prevents the UI from freezing during long operations.
- 
**Modern JavaScript** : Aligns with promises and`async/await` for cleaner code.
- 
**Recommended by Microsoft** : Asynchronous execution is the default and preferred approach.

### Example: Retrieving a Record Asynchronously

```
Xrm.WebApi.retrieveRecord("account", "a8a19cdd-88df-e311-b8e5-6c3be5a8b200", "?$select=name")
  .then((result) => {
    console.log(`Account Name: ${result.name}`);
  })
  .catch((error) => {
    console.error(`Error: ${error.message}`);
  });
```
Using `async/await` for a more modern syntax:


```
async function getAccountName() {
  try {
    const result = await Xrm.WebApi.retrieveRecord("account", "a8a19cdd-88df-e311-b8e5-6c3be5a8b200", "?$select=name");
    console.log(`Account Name: ${result.name}`);
  } catch (error) {
    console.error(`Error: ${error.message}`);
  }
}
getAccountName();
```
### When to Use Asynchronous Calls

- Most scenarios in Dynamics 365, especially UI-related scripts.
- Operations where responsiveness matters (e.g., form events).
- Long-running requests where blocking the thread would harm usability.

## Synchronous Xrm.WebApi Calls

While `Xrm.WebApi` is asynchronous by default, you can make synchronous calls using the `Xrm.WebApi.online.execute()` method with a custom request. This approach blocks execution until the server responds, which can be useful in specific cases but comes with caveats.

### Why Use Synchronous Calls?

- 
**Sequential Logic** : Ensures one operation completes before the next begins.
- 
**Simpler Flow** : Avoids nested promises or callbacks in rare cases.
- 
**Legacy Compatibility** : Matches older synchronous workflows (e.g., pre-promise code).

### Example: Retrieving a Record Synchronously

To make a synchronous call, you’ll need to craft a custom request and use `execute()` with the `isAsync` flag set to `false`:


```
function retrieveAccountSync() {
  const request = {
    entityName: "account",
    entityId: "a8a19cdd-88df-e311-b8e5-6c3be5a8b200",
    getMetadata: function () {
      return {
        boundParameter: null,
        parameterTypes: {},
        operationType: 2, // Retrieve operation
        operationName: "Retrieve"
      };
    }
  };
  const response = Xrm.WebApi.online.execute(request, { async: false });
  if (response.ok) {
    const result = JSON.parse(response.responseText);
    console.log(`Account Name: ${result.name}`);
  } else {
    console.error(`Error: ${response.statusText}`);
  }
}
retrieveAccountSync();
```
**Note**: This requires additional setup (e.g., parsing the response manually) and isn’t as straightforward as the built-in CRUD methods.

### When to Use Synchronous Calls

- Rare cases where order of execution is critical (e.g., before a form save).
- Scripts running in the background without UI impact.
- Situations where asynchronous complexity outweighs the benefits.

## Synchronous vs. Asynchronous: A Quick Comparison

| Feature | Asynchronous | Synchronous | 
|---|---|---|
| **Execution** | Non-blocking (promise-based) | Blocking (waits for response) | 
| **Ease of Use** | High (built-in methods) | Moderate (custom setup) | 
| **Performance Impact** | Minimal (UI stays responsive) | High (UI may freeze) | 
| **Best For** | Most Dynamics 365 scenarios | Specific sequential logic | 

## Best Practices

1. 
**Default to Asynchronous** : Stick with asynchronous calls unless you have a compelling reason not to. They’re safer, more modern, and better for user experience.
2. 
**Avoid Synchronous in UI Scripts** : Blocking the thread can freeze forms, frustrating users—reserve synchronous calls for non-UI contexts.
3. 
**Use `async/await`** : For asynchronous calls, prefer`async/await` over`.then()` for readability and error handling.
4. 
**Test Thoroughly** : Synchronous calls can introduce race conditions or performance issues—test them in your specific environment.

## Final Thoughts

In most Dynamics 365 projects, **asynchronous `Xrm.WebApi` calls** are the way to go. They align with modern JavaScript practices, keep your UI responsive, and are easier to implement with built-in methods. **Synchronous calls**, while available, should be a last resort due to their complexity and potential downsides.

## Top comments (0)