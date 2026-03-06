import pandas as pd
import regex as re
from sklearn.feature_extraction.text import CountVectorizer
def task_func(text):
    """
    Analyze a text by creating a document term matrix with CountVectorizer. The text contains several sentences, each separated by a period.
    Ignore empty sentences.

    Parameters:
    text (str): The text to analyze.

    Returns:
    DataFrame: A pandas DataFrame with the document-term matrix. Its column names should be adapted from the vectorizer feature names.

    Requirements:
    - pandas
    - regex
    - sklearn.feature_extraction.text.CountVectorizer

    Example:
    >>> text = "This is a sample sentence. This sentence contains sample words."
    >>> dtm = task_func(text)
    >>> print(dtm)
       contains  is  sample  sentence  this  words
    0         0   1       1         1     1      0
    1         1   0       1         1     1      1
    """
    # TODO: Implement the task
    # Hint: Use the CountVectorizer from sklearn.feature_extraction.text
    # Hint: Use the regex library to split the text into sentences
    # Hint: Use the regex library to split the sentences into words
    # Hint: Use the regex library to remove empty sentences
    # Hint: Use the regex library to remove punctuation
    # Hint: Use the regex library to remove stopwords
    # Hint: Use the regex library to remove numbers
    # Hint: Use the regex library to remove non-alphanumeric characters
    # Hint: Use the regex library to remove short words
    # Hint: Use the regex library to remove long words
    # Hint: Use the regex library to remove words with a length of 1
    # Hint: Use the regex library to remove words with a length of 2
    # Hint: Use the regex library to remove words with a length of 3
    # Hint: Use the regex library to remove words with a length of 4
    # Hint: Use the regex library to remove words with a length of 5
    # Hint: Use the regex library to remove words with a length of 6
    # Hint: Use the regex library to remove words with a length of 7
    # Hint: Use the regex library to remove words with a length of 8
    # Hint: Use the regex library to remove words with a length of 9
    # Hint: Use the regex library to remove words with a length of 10
    # Hint: Use the regex library to remove words with a length of 11
    # Hint: Use the regex library to remove words with a length of 12
    # Hint: Use the regex library to remove words with a length of 13
    # Hint: Use the regex library to remove words with a length of 14
    # Hint: Use the regex library to remove words with a length of 15
    # Hint: Use the regex library to remove words with a length of 16
    # Hint: Use the regex library to remove words with a length of 17
    # Hint: Use the regex library to remove words with a length of 18
    # Hint: Use the regex library to remove words with a length of 19
    # Hint: Use the regex library to remove words with a length of 20
    # Hint: Use the regex library to remove words with a length of 21
    # Hint: Use the regex library to remove words with a length of 22
    # Hint: Use the regex library to remove words with a length of 23
    # Hint: Use the regex library to remove words with a length of 24
    # Hint: Use the regex library to remove words with a length of 25
    # Hint: Use the regex library to remove words with a length of 26
    # Hint: Use the regex library to remove words with a length of 27
    # Hint: Use the regex library to remove words with a length of 28
    # Hint: Use the regex library to remove words with a length of 29
    # Hint: Use the regex library to remove words with a length of 30
    # Hint: Use the regex library to remove words with a length of 31
    # Hint: Use the regex library to remove words with a length of 32
    # Hint: Use the regex library to remove words with a length of 33
    # Hint: Use the regex library to remove words with a length of 34
    # Hint: Use the regex library to remove words with a length of 35
    # Hint: Use the regex library to remove words with a length of 36
    # Hint: Use the regex library to remove words with a length of 37
    # Hint: Use the regex library to remove words with a length of 38
    # Hint: Use the regex library to remove words with a length of 39
    # Hint: Use the regex library to remove words with a length of 40
    # Hint: Use the regex library to remove words with a length of 41
    # Hint: Use the regex library to remove words with a length of 42
    # Hint: Use the regex library to remove words with a length of 43
    # Hint: Use the regex library to remove words with a length of 44
    # Hint: Use the regex library to remove words with a length of 45
    # Hint: Use the regex library to remove words with a length of 46
    # Hint: Use the regex library to remove words with a length of 47
    # Hint: Use the regex library to remove words with a length of 48
    # Hint: Use the regex library to remove words with a length of 49
    # Hint: Use the regex library to remove words with a length of 50
    # Hint: Use the regex library to remove words with a length of 51
    # Hint: Use the regex library to remove words with a length of 52
    # Hint: Use the regex library to remove words with a length of 53
    # Hint: Use the regex library to remove words with a length of 54
    # Hint: Use the regex library to remove words with a length of 55
    # Hint: Use the regex library to remove words with a length of 56
    # Hint: