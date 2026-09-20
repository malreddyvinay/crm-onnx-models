With Microsoft providing us more flexibility with Power Automate (MS Flow), we can now retrieve **working days and holiday details of the CRM Service Calendar** directly within Power Automate flows. Previously we used Plugins or JavaScript to get Calendar’s working days and holiday details, but now they can be directly retrieved through the Power Automate (flow) as well.

Recently, we got a requirement to check whether a specific date is a business/working day considering weekends and public holidays defined in the Service calendar of CRM.

Below are the workdays defined in the CRM:

Below is the list of holidays defined in the CRM which are observed:

Given a specific date, we were supposed to check whether it is a working day considering the weekends and public holidays defined above.

## **The Power Automate Flow steps to get Working Days per week**

### **Step 1****: Retrieve Calendar (Customer Service Type)**

First, add the ‘List Records’ step to retrieve the ‘Customer Service’ type Calendar. Use a filter query to fetch the calendar by its name and type. To capture the necessary GUID for the next step.

### **Step 2****: Retrieve Calendar (Working Days)**

Now, proceed to fetch the working days for the previously obtained calendar. Utilize an ‘Apply to Each’ step to iterate through each calendar, and within that, add a ‘Get a Row by ID’ action to retrieve the working day’s calendar using the expand query. The expanded query allows us to seamlessly expand related tables in the list rows action. In this case, the main table is Calendar while the related table is Calendar Rules where the weekly working days pattern is stored.

In the ‘Compose’ action, we can find the calendar working days enumerated. Using the following formula:

```
If (    empty(outputs('Get_a_Calendar_which_contains_working_days')?['body/calendar_calendar_rules'][0]?['pattern']),
-1,
Substring (      outputs('Get_a_Calendar_which_contains_working_days')?['body/calendar_calendar_rules'][0]?['pattern'],        add(indexOf(outputs('Get_a_Calendar_which_contains_working_days')?['body/calendar_calendar_rules'][0]?['pattern'], 'BYDAY='),
length('BYDAY='))
)
)
```
## **The Power Automate Flow steps to get Holidays**

### **Step 1****: Retrieve Calendar (Holiday Schedule Type)**

First, use the ‘List Records’ step to retrieve the ‘Holiday Schedule’ type Calendar. Apply a filter query to fetch the calendar by its name and type. The result will provide the necessary GUIDs for the next step.

### **Step 2****: Retrieve Calendar Rules (Holidays)**

Now, proceed to fetch the calendar rules for the previously obtained calendar. Utilize an ‘Apply to Each’ step to iterate through each calendar, and within that, add a ‘Get a Row by ID’ action to retrieve the calendar rule.

However, note that attempting to fetch the calendar rule directly will result in an error saying “The ‘Retrieve’ method does not support entities of type ‘calendarrule’”,

As a workaround, we can retrieve the calendar rules along with calendar data using the expand query.

In the ‘Compose’ action, we can find the calendar rules enumerated using the following formula:

outputs(‘Get_a_calendar_which_contains_holidays’)?[‘body/calendar_calendar_rules’]

### **Step 3****: Get Holidays details**

For each calendar rule, implement an ‘Apply to Each’ loop. Within this loop, incorporate a Compose action to extract the holiday name, as illustrated.

## **Conclusion**

Using Power Automate, we can retrieve Calendar and Calendar Rule details which allows users to handle complex requirements, such as checking working days while considering weekends and defined holidays.