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
        # Remove leading and trailing whitespaces
        sentence = sentence.strip()
        # Check if the sentence is not empty
        if sentence:
            # Split the sentence into words
            words = sentence.split()
            # Filter out the stopwords
            filtered_words = [word for word in words if word not in STOPWORDS]
            # Count the number of words that are not stopwords
            word_count = len(filtered_words)
            # Add the sentence and its word count to the dictionary
            result_dict[f"Sentence {i}"] = word_count
    # Create a pandas Series from the dictionary
    result_series = pd.Series(result_dict)
    return result_series