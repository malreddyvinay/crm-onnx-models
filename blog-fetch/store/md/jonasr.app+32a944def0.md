***Using Bulk Data Updater can be a bit scary…*** ????***Which records did I update?*** ????***Which fields did I change?*** ????***What did really happen??*** ????

I have a soft spot in my heart, and the spot is **logging**… ???? I’m not a big fan of logs ????, but I’m a fan of logs ????. If you have read about **Canary**, you know.

The **Bulk Data Updater** can do many things, doing it in milliseconds and without any rollback. **Scary, right?**

That is why I have for a long time – too long time – I wanted to be able to **see all the nitty-gritty details about WHAT ACTUALLY HAPPENED??**

## To me – this is a huge new feature!

But yes yes, I agree, it’s no ***new*** feature. The tool does what it already did. But **logging**… man, those give me goosebumps!

What happened – the logging – can be saved by clicking the button (weird name or not?) **Save Log…** next to the execution button. It will, by default, save a **CSV** file, which is (probably, hopefully…) easy to open in **Excel**.

From version **1.2024.9.2** or later, **everything** is logged. See this short video:

### Even more details

For every execution they are stored in XML files, very technical files. Find the folder by in XrmToolBox go to Settings, Paths, and open the storage folder.

In the folder “Logs” the XML files are found. The names are similar to **BDU_Update_rapp_rocket_20240919_164253.log**

The format is **BDU_<action>_<table>_<date>_<time>.log**

It starts with general info about what to do and how long it took etc.

```
<BDULogRun>
  <TimeStamp>2024-09-19T16:42:53.4251873+02:00</TimeStamp>
  <Action>Update</Action>
  <EntityLogicalName>rapp_rocket</EntityLogicalName>
  <EntityDisplayName>Rocket</EntityDisplayName>
  <DurationMS>3957.4824000000003</DurationMS>
  <Records>18</Records>
  <Errors>0</Errors>
  <Requests>
```
Then this is details about one request to the server:

```
    <BDULogRequest>
      <TimeStamp>2024-09-19T16:42:53.4281883+02:00</TimeStamp>
      <No>1</No>
      <Request>UpdateMultiple</Request>
      <Id>d368f5f9-dc19-4cc0-b020-de749666a2fb</Id>
      <DurationMS>2304.9274</DurationMS>
      <Success>true</Success>
      <Records>
```
And this is one Record:

```
        <BDULogRecord>
          <Id>843471ab-717b-ec11-8d21-6045bd8a4289</Id>
          <Name>Apollo 12</Name>
          <Attributes>
            <BDULogAttribute>
              <LogicalName>rapp_description</LogicalName>
              <DisplayName>Description</DisplayName>
              <Action>Calc</Action>
              <NewValue xsi:type="xsd:string">Apollo 12 (562)</NewValue>
              <NewValueString>Apollo 12 (562)</NewValueString>
              <OldValue xsi:type="xsd:string">990:
Apollo 12</OldValue>
              <OldValueString>990:
Apollo 12</OldValueString>
              <OldValueKnown>true</OldValueKnown>
            </BDULogAttribute>
            <BDULogAttribute>
              <LogicalName>statuscode</LogicalName>
              <DisplayName>Status Reason</DisplayName>
              <Action>Set</Action>
              <NewValue xsi:type="OptionSetValue">
                <Value>1</Value>
              </NewValue>
              <NewValueString>Idle</NewValueString>
              <OldValue xsi:type="OptionSetValue">
                <Value>100000000</Value>
                <ExtensionData />
              </OldValue>
              <OldValueString>Never Again</OldValueString>
              <OldValueKnown>true</OldValueKnown>
            </BDULogAttribute>
            <BDULogAttribute>
              <LogicalName>importsequencenumber</LogicalName>
              <DisplayName>Import Sequence Number</DisplayName>
              <Action>Set</Action>
              <NewValue xsi:type="xsd:int">240919211</NewValue>
              <NewValueString>240919211</NewValueString>
              <OldValueKnown>false</OldValueKnown>
            </BDULogAttribute>
          </Attributes>
        </BDULogRecord>
```
Enough details? I just love it… ????