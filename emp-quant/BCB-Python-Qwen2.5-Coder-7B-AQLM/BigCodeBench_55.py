
import re
import pandas as pd
STOPWORDS = ["Those", "are", "the", "words", "to", "ignore"]

def task_func(text):
    # Split the text into sentences using regular expression
    sentences = re.split(r'[.!?]', text)
    
    # Initialize an empty dictionary to store the results
    result_dict = {}
    
    # Iterate over the sentences
    for i, sentence in enumerate(sentences, start=1):
        # Remove leading and trailing whitespace
        sentence = sentence.strip()
        
        # Skip empty sentences
        if not sentence:
            continue
        
        # Split the sentence into words
        words = sentence.split()
        
        # Filter out stopwords
        filtered_words = [word for word in words if word not in STOPWORDS]
        
        # Count the number of words in the filtered sentence
        word_count = len(filtered_words)
        
        # Add the sentence and its word count to the dictionary
        result_dict[f"Sentence {i}"] = word_count
    
    # Convert the dictionary to a pandas Series
    result_series = pd.Series(result_dict)
    
    return result_series