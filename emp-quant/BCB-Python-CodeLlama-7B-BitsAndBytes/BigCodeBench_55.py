
import re
import pandas as pd
STOPWORDS = ["Those", "are", "the", "words", "to", "ignore"]
def task_func(text):
    # Split the text into sentences
    sentences = re.split(r'[.!?]', text)

    # Create a dictionary to store the number of words in each sentence
    sentence_counts = {}

    # Iterate over the sentences and count the number of words
    for i, sentence in enumerate(sentences):
        # Remove any stopwords from the sentence
        sentence_words = [word for word in sentence.split() if word.lower() not in STOPWORDS]

        # Add the sentence to the dictionary with its word count
        sentence_counts[f"Sentence {i+1}"] = len(sentence_words)

    # Create a pandas Series from the dictionary
    sentence_series = pd.Series(sentence_counts)

    return sentence_series