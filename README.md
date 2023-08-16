# ChatGPT-Review-Analyzer
This program uses the ChatGPT API to analyze reviews. Users can choose between the Single Review Analyzer and the Multiple Review Analyzer. Using the single version will print out a predicted rating, analysis, and list of tags. Using the Multiple Review Analyzer will require reviews to be in a text file separated by a completely blank line. The program will then write to 2 other text files. One file will contain the reviews, their rating, analysis, and tags. The other file will contain the tags from all of the reviews and will be ordered by frequency.

Below is an example:

The following is a 5 star review by Mathias Lopez on the Sony ZX series Wired On-Ear headphones. (https://www.amazon.com/product-reviews/B00NJ2M33I/ref=cm_cr_unknown?ie=UTF8&filterByStar=five_star&reviewerType=all_reviews&pageNumber=1#reviews-filter-bar)

Review: I've been using these for a couple months now. They're pretty comfortable, the padding on the earpieces is really nice and feels high-quality. The sound quality is also pretty good! It comes with an app you can install on your phone that lets you change different sound settings, allowing for a lot of variety when it comes to specific songs or media types (higher bass, better eq, etc.). These are supposed to be noise cancelling and I guess they kind of do that? Not much more noise cancelling that traditional headphones I would say however.
The bluetooth range for these is pretty far, it works with my phone from all the way across the house, which is nice. I would recommend if you want a nice pair of wireless headphones, pretty good.

Predicted Rating:
 4

Analysis: The reviewer has been using these headphones for a couple of months and finds them comfortable, thanks to the high-quality padding on the earpieces. They also mention that the sound quality is pretty good and appreciate the flexibility offered by the app, which allows for different sound settings. However, they note that the noise-canceling feature is not significantly better than traditional headphones. On the positive side, the Bluetooth range is impressive, as it works from all the way across the house. Overall, the reviewer recommends these headphones as a nice pair of wireless headphones.

Predicted Tags: 
-comfortable
-high-quality padding
-good sound quality
-customizable sound settings
-noise cancelling (to a certain extent)
-long bluetooth range
-recommendable for wireless headphones




**Limitations**
- The program will take some time to run the requests to the model, non subscribed users have a max of 3 requests per minute.


**Important information:**

The pricing for using the ChatGPT API can be found here: https://openai.com/pricing

Reviews will be given a predicted rating, analysis, and predicted tags.

Two files will be written to, one with the review, the predicted rating, analysis, and predicted tags for each review, the other with a list of all the tags across the reviews, sorted from most occurring to least.

Your reviews should have a completely blank line between each review.

More information on the API can be found here: https://platform.openai.com/docs/introduction/overview
