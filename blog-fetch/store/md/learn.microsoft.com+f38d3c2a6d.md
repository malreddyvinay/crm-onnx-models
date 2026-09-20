Note

Access to this page requires authorization. You can try signing in or changing directories.

Access to this page requires authorization. You can try changing directories.

Returns a reference to the object that the event occurred on.

## Syntax

`ExecutionContextObj.getEventSource()`

## Return value

**Type**: Object

**Description**: Returns the object from the **Xrm** object model that is the source of the event, not an HTML DOM object. For example, in an OnChange event, this method returns an item from the **formContext.data.entity.attributes**  collection that represents the changed column.

| Events | Return Object | 
|---|---|
| OnChange | column | 
| OnDataLoad | formContext.data.entity | 
| OnGridDataLoad | SubGrid control | 
| OnLoad | formContext.ui | 
| OnLookupTagClick | Lookup control | 
| OnPostSearch | kbSearch control | 
| OnProcessStatusChange | formContext.data.process | 
| OnProcessStatusChange | formContext.data.process | 
| OnReadyStateComplete | IFrame control | 
| OnRecordSelect | formContext.data.entity | 
| OnResultOpened | kbSearch control | 
| OnSave | formContext.data.entity | 
| OnPostSave | None | 
| OnSelection | None | 
| OnStageChange | formContext.data.process | 
| OnStageSelected | formContext.data.process | 
| OnTabStateChange | tab object | 
| PreSearch | Lookup control |