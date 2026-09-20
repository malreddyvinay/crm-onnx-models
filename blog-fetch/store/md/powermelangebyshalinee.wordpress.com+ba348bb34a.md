**Business Requirement:** We have two tables- Cluster Identifier & Primary Skills having N:N relationship between them. The requirement was as soon as a Cluster Identifier is selected, we had to list all the related skills and store it in a separate field concatenated with commas.

**Solution**: We will write a Power Automate as follows:

**Step 1**: Get a Row By ID to get the Cluster Identifier selected.

**Step 2**: List all Primary Skills. This we can do by listing all records of the intermediate table built to store all the values. 

***Theory***: This table is not exposed on the frontend but can be accessed by using the Entity Name of the N:N relationship as shown in the image below and concatenating the word “set” at the end with the cluster identifier record id equalization.

If you check the JSON output of this step, it will come like this:

 "value": [

{

"@odata.type": "#Microsoft.Dynamics.CRM.wip_wip_clusteridentifier_wip_primaryskill",

"@odata.id": "https://orgfbaa0000.crm.dynamics.com/api/data/v9.1/wip_wip_clusteridentifier_wip_primaryskillset(*5a70ef1-6cbf-ee11-9079-002248d5dd0*)",

"@odata.editLink": "wip_wip_clusteridentifier_wip_primaryskillset(*5a70ef1-6cbf-ee11-9079-002248d5dd0*)",

"versionnumber@OData.Community.Display.V1.FormattedValue": "13,472,112",

"versionnumber@odata.type": "#Int64",

"versionnumber": 13472112,

"wip_clusteridentifierid@odata.type": "#Guid",

"wip_clusteridentifierid": "23364903-99ba-ee11-907a-002248d5dbc4",

"wip_primaryskillid@odata.type": "#Guid",

"wip_primaryskillid": "ff22d2c9-5cbf-ee11-9079-002248d5d19f",

"wip_wip_clusteridentifier_wip_primaryskillid@odata.type": "#Guid",

"wip_wip_clusteridentifier_wip_primaryskillid": "05a70ef1-6cbf-ee11-9079-002248d5dd06"

}

Thus we see in this table, it stores the Guid of both Cluster Identifier & Skill table for all related skills.

**Step 3**: Then do a Apply to Each in these skills and get the Primary Skill table name using Primary skill id and Append to an array variable

**Step 4**: Lastly when out of the loop, use the compose step with expression join(variables(‘Primary Skill ID’), ‘,’)

***Tip***: Usually when we use “concatenate” to append the skills to add a comma towards the end of string, at the end we have to again remove the last one, so this “join” option is a better feature where we can use the outputs directly.

Hope it helps!

& the ***Power Affirmation*** for the day is:*“I am constantly growing and evolving into a better person”*