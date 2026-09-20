Hi Amazing people!

Today i have got one of the recent requirements i came through.

***Business Requirement***: We had a string coming from a source which had to be compared with the account name and then further actions had to be followed. But certain accounts had special characters in it like “&” in “Larsen & Toubro” and other special characters.

***Problem Faced:*** While writing the Fetch XML of comparison in “List Rows” action, if such special characters are present in the Account name, it throws an “Invalid XML” error.

Handling them on a case by case basis would be a nightmare plus its not the correct solution. So i digged into the functions available in Power Automate and found a life saviour – **EncodeURIComponent()**

***Discussion:*** This function encodes a URI by replacing each instance of certain characters by one, two, three, or four escape sequences representing the UTF-8  encoding of the character.

It is widely used to return a string that replaces URL-unsafe characters with escape characters but can be utilised in such cases too. Let us see how!

***Solution:*** Encode the string to be compared before sending it to fetch or within the Fetch itself.

PS: the Account name! Well i am awesome 😉

It will convert the special characters with escape characters like below:

Best part, it works for most of the special characters in use. Voila! Your flow runs successfully now:

Hope it helps!

& the Power Affirmation of the day is:

“I am proud of myself and my achievements”

This is super helpful and smart. Thank you for sharing.

LikeLike