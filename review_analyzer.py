import os
import openai
import time
import sys

class ReviewAnalyzer:
    def __init__(self, key: str):
        openai.api_key=key
        
    def singleReview(self, review: str):
        r = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You may only answer with a single number."}, 
                {"role": "user", "content": "What rating between 0 and 5 inclusive do you think this reviewer would give based on their review: "+review+"/n Give only the number."}
            ]
        )
            
        t = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You may only answer with a list in the format of: -item1\n-item2"}, 
                {"role": "user", "content": "Summarize the main points of this review into a list of generic tags: "+review}
            ]
        )
            
        f = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"}, 
                {"role": "user", "content": "Give me a summary of feedback from this review: "+review}
            ]
        )
        predicted_rating = r.choices[0].message.content
        time.sleep(20)
        predicted_tags= t.choices[0].message.content
        time.sleep(20)
        predicted_feedback= f.choices[0].message.content
        return [predicted_rating, predicted_tags, predicted_feedback]
    


    def multiReview(self, reviews: list):
        rating_predictions=[]
        analysis=[]
        tagging=[]
        for review in reviews:
            
            #Initialization of the models with the review
            
            r = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You may only answer with a single number."}, 
                {"role": "user", "content": "What rating between 0 and 5 inclusive do you think this reviewer would give based on their review: "+review+"/n Give only the number."}
            ]
            )
            
            t = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You may only answer with a list in the format of: -item1\n-item2"}, 
                {"role": "user", "content": "Summarize the main points of this review into a list of generic tags: "+review}
            ]
            )
            
            f = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"}, 
                {"role": "user", "content": "Give me a summary of feedback from this review: "+review}
            ]
            )
            
            #Calling the models for chatgpt's answer; each call must be staggered to work within the number of calls per minute
            
            rating = r.choices[0].message.content
            time.sleep(20)
            tags= t.choices[0].message.content
            time.sleep(20)
            feedback= f.choices[0].message.content
            time.sleep(20)
            
            #add the answers to an array of stings
            
            rating_predictions.append(rating)
            analysis.append(feedback)
            tagging.append(tags)
        
        return [rating_predictions, analysis, tagging]



    def reviewFile(self, file_path_reviews: str, file_path_analysis: str):
        try:
            with open(file_path_reviews, "r") as file:
                content = file.read()
            reviews = content.split("\n\n")
            reviews = [review.strip() for review in reviews]
        except:
            print("Error occured with file path: ", file_path_reviews)
        
        rating_predictions, analysis, tagging = self.multiReview(reviews)

        try:
            with open(file_path_analysis, "w") as file:
                for r, c, a, t, in zip(reviews, rating_predictions, analysis, tagging):
                    file.write("Review: "+r+"\n\n")
                    file.write("Predicted Rating:\n "+c+"\n\n")
                    file.write("Analysis: "+a+"\n\n")
                    file.write("Predicted Tags: \n"+t+"\n\n")
        except:
            print("Error occured with file path: ", file_path_analysis)


    if __name__ == '__main__':
        if len(sys.argv)<3:
            print("usage: python review_analyzer <key> <type> <args>")
        else:    
            try:
                reviewanalyzer=ReviewAnalyzer(sys.argv[1])
                if sys.argv[2]=='single':
                    try:
                        reviewanalyzer.singleReview(sys.argv[3])
                    except:
                        print("usage: python review_analyzer <key> single <review>")
                elif sys.argv[2]=='multi':
                    try:
                        reviewanalyzer.multiReview(sys.argv[3:])
                    except:
                        print("usage: python review_analyzer <key> multi <review1> <review3> <review3> ...")
                elif sys.argv[2]=='file':
                    try:
                        reviewanalyzer.reviewFile(sys.argv[3], sys.argv[4])
                    except:
                        print("usage: python review_analyzer <key> file <file_read_path> <file_write_path>")
            except:
                print("usage: python review_analyzer <key> <type> <args>")