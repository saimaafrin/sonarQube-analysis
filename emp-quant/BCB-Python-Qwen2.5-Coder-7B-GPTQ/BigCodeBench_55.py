import re
import pandas as pd
STOPWORDS = ["Those", "are", "the", "words", "to", "ignore"]
def task_func(text):
    # Split the text into sentences using regular expression
    sentences = re.split(r'(?<=[.!?]) +', text)
    
    # Initialize an empty dictionary to store the results
    result_dict = {}
    
    # Iterate over the sentences
    for i, sentence in enumerate(sentences, start=1):
        # Split the sentence into words and filter out stopwords
        words = [word for word in sentence.split() if word not in STOPWORDS]
        
        # Check if the sentence is not empty after filtering stopwords
        if words:
            # Store the sentence and its word count in the dictionary
            result_dict[f"Sentence {i}"] = len(words)
    
    # Convert the dictionary to a pandas Series
    result_series = pd.Series(result_dict)
    
    return result_series