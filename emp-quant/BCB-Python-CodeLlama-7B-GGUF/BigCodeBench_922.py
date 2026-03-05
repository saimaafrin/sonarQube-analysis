
import pandas as pd
import re

# Constants
STOPWORDS = set([
    "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
    "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
    "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
    "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had",
    "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because",
    "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into",
    "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out",
    "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where",
    "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no",
    "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just",
    "don", "should", "now"
])

def task_func(data, column):
    """
    Removes English stopwords from a text column in a DataFrame and returns the modified DataFrame.

    Parameters:
    data (pandas.DataFrame): The DataFrame containing the text column to be processed.
    column (str): The name of the text column to be processed.

    Returns:
    pandas.DataFrame: A DataFrame with the stopwords removed from the specified column.
    """
    # Create a copy of the original DataFrame
    data_copy = data.copy()

    # Remove stopwords from the specified column
    data_copy[column] = data_copy[column].apply(lambda x: " ".join([word for word in x.split() if word.lower() not in STOPWORDS]))

    return data_copy