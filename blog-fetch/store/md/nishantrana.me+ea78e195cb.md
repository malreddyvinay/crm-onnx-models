Let us fetch 5000 contact records using List Rows, and then update it using Apply To Each.

It took around – 37 minutes

Now let us enable **concurrency** **control** for **Apply To Each** action, and let it run under **20** (default) degree of parallelism.

This time it took around **4 minutes.**

Let us increase it to the maximum this time, i.e. 50.

This time it took around **2:45 minutes.**

Thus Concurrency Control option can help in processing records faster by processing records in parallel instead of one by one by using parallel threads. However, if the ordering of the way records need to be processed is critical, then we need to be careful before using it and also at times it can cause the API’s request limit to be hit.

Get more details on Concurrency limits

Hope it helps..

### Discover more from Nishant Rana's Weblog

Subscribe to get the latest posts sent to your email.

## One thought on “Concurrency Control – Apply to each for improving performance (Power Automate / Dataverse)”