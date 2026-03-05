import pandas as pd
import re
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
    data (pandas.DataFrame): The DataFrame containing the text column.
    column (str): The name of the text column to be processed.

    Returns:
    pandas.DataFrame: A DataFrame with the stopwords removed from the specified column.
    """
    # Create a new column with the stopwords removed
    data[column + "_stopwords_removed"] = data[column].str.lower().str.split().apply(lambda x: [word for word in x if word not in STOPWORDS])

    # Return the modified DataFrame
    return data
data = pd.DataFrame({"text": ["This is a test sentence.", "This is another test sentence."]})