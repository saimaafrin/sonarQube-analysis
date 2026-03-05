import re
import pandas as pd
STOPWORDS = ["Those", "are", "the", "words", "to", "ignore"]
def task_func(text):
    # Split the text into sentences using regex
    sentences = re.split(r'[.!?]\s*', text)
    # Initialize an empty dictionary to store the results
    result_dict = {}
    # Iterate over the sentences
    for i, sentence in enumerate(sentences, start=1):
        # Remove leading and trailing whitespace
        sentence = sentence.strip()
        # Check if the sentence is not empty
        if sentence:
            # Split the sentence into words and filter out stopwords
            words = [word for word in sentence.split() if word not in STOPWORDS]
            # Count the number of words
            word_count = len(words)
            # Add the sentence and word count to the dictionary
            result_dict[f"Sentence {i}"] = word_count
    # Convert the dictionary to a pandas Series
    result_series = pd.Series(result_dict)
    return result_series