There are two different onLoad events in the client-side XRM framework, and I did not know that… Well, it’s better to find it out late than never 😊

Here is how it works:

- **OnDataLoad** happens on on initial page load, when formContext.data.refresh is called, or when the data is saved and there is a change
- **OnLoad** , on the other hand, is called on initial page load, and, also, when a new record is first saved

Actually, I used to think OnLoad does what OnDataLoad do. Maybe it used to do it? Not sure.

Either way, when specifying an event handler in the form designer, you are specifying OnLoad event handler (so it’s formContext.ui):

It won’t trigger when you call formContext.data.refresh eventually, so, if you need something to happen after the refresh, you may need to attach one more event from code:

In the onload, you can use formContext.data.addOnLoad, and the function you pass as an argument will be called right away (after the onLoad), and, also, whenever you use formContext.data.refresh, for instance.