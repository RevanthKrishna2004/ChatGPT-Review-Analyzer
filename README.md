# ChatGPT-Review-Analyzer
This program uses the ChatGPT API to analyze reviews.

Usage:
- Run the blocks of code in the ChatGPT Review Analyzer.ipynb file
- You will be prompted to enter the file path for the file with the reviews, and the two files the program should write to for the full analysis (rating, analysis, and tags), and one for the organized tags from all the reviews
- You will then be asked to enter your API key
- The program will take some time to run the requests to the model, free users have a max of 3 requests per minute.


**Important information:**

The pricing for using the ChatGPT API can be found here: https://openai.com/pricing

Reviews will be given a predicted rating, analysis, and predicted tags.

Two files will be written to, one with the review, the predicted rating, analysis, and predicted tags for each review, the other with a list of all the tags across the reviews, sorted from most occurring to least.

Your reviews should have a completely blank line between each review.

More information on the API can be found here: https://platform.openai.com/docs/introduction/overview
