## How to resize images with Cloud Flows

# How to resize images with Cloud Flows

How to resize images with Cloud Flows in my opinion should be useful for many scenarios, let me know where it was useful for you.

Scenario where I faced the need to resize images:

For many companies, Health & Safety, Quality topics requires inspections. Inspectors are making photo/s and when the inspection finish (in most of the cases) report should be automatically generated (the best with the photos in the body of report) to the stakeholders.

I will focus on the part where I need to generate report = I will use Power Automate.

If I want to do it with Standard connectors / for “free” I’m **limited to the 2MB size of the converted file**. And I think I don’t need to stress out how big photos done with modern phones can get 😭

Resolution is to stay under the limit of 2 MB by resizing the pictures 🤩 If that sounds interesting & you want to learn how to do it, Let’s go!

## Idea of solution

I’m not aware that there is out of the box action to resize pictures, but I know that every document / picture which is uploaded to the SharePoint library is getting Thumbnails generated:

Knowing that, I start to wonder how I can utilize that fact. When I click the URL of the thumbnail, it displays document / picture 😍

Hint:

For Power Apps to display images correctly in mobile Power Apps player, the reference to Thumbnails is the correct way. 

Interesting is that attachments which are added directly to the lists are not having the thumbnails. This makes the next why I don’t like to keep documents as attachments in lists.

## Solution

I was looking for the option to use or download the thumbnails. Finally, I found it 🤩 I learn about it by watching Shane’s Young video: QR Codes in Power Apps – Create, Download, PDF, and Email! It was pure accident as the video is one year old. Moreover, It proves two things for me:

1. Learning is fun and learning new stuff might return with great impact at various moments and not instantly
2. Need to catch up with my learnings – to long to watch / to read list 😭

I know that you will watch the video, but I will allow myself to take the key part which was important for my solution. Which is One Drive action, Upload file from URL. With Upload file form URL I can take the thumbnail URL and use it to create a new file which will be resized 🤯

Thumbnails have the following dimensions:

- Large – 800 x 800 px
- Medium – 176 x 176 px
- Small – 96 x 96 px

## Bonus

During making preparations to *How to resize images with Cloud Flows*, I notice one more useful action from OneDrive Get file thumbnail:

Note:

Thumbnail generate in this way is valid only for 6 hours

I think it is giving an extra boost to the whole idea. You can generate the thumbnail if you will upload the document to the OneDrive and then use the results of the Get file thumbnail to Upload the file from URL to keep the resize image 🤩

## Summary

I hope *How to resize images with Cloud Flows* will be useful. Although I know it is not 100% resizing, where we do have full control over the size result of the dimensions. But after all, it is for “free” and for me, it was good enough 😜

I wonder 🤔 if there is a method to Get file thumbnail, if that might be hijacked to get better control over the results? Maybe material for the next investigation?