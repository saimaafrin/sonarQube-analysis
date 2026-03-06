
import re
import pandas as pd

STOPWORDS = ["Those", "are", "the", "words", "to", "ignore"]

def task_func(text):
    # Split the text into sentences using regular expression
    sentences = re.split(r'[.!?]', text)
    
    # Initialize an empty dictionary to store the results
    result_dict = {}
    
    # Iterate over the sentences
    for i, sentence in enumerate(sentences):
        # Strip leading/trailing whitespace and split into words
        words = [word.strip() for word in sentence.split()]
        
        # Filter out stopwords
        filtered_words = [word for word in words if word not in STOPWORDS]
        
        # Count the number of words that are not stopwords
        num_words_no_stopwords = len(filtered_words)
        
        # Add to the dictionary with a formatted key
        result_dict[f"Sentence {i+1}"] = num_words_no_stopwords
    
    # Convert the dictionary to a pandas Series
    result_series = pd.Series(result_dict)
    
    return result_series