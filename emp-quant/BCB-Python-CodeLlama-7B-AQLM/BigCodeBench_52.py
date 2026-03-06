import pandas as pd
import regex as re
STOPWORDS = ["a", "an", "the", "in", "is", "are"]
def task_func(text):
    """
    Count the frequency of each word in a text after removing specific stopwords.

    Parameters:
    text (str): The text to analyze.

    Returns:
    Series: A pandas Series with word frequencies excluding the words in STOPWORDS list.

    Requirements:
    - pandas
    - regex

    Example:
    >>> text = "This is a sample text. This text contains sample words."
    >>> word_counts = task_func(text)
    >>> print(word_counts)
    this        2
    sample      2
    text        2
    contains    1
    words       1
    dtype: int64
    """
    # Remove stopwords
    text = re.sub(r"\b(" + "|".join(STOPWORDS) + r")\b", "", text, flags=re.IGNORECASE)

    # Split text into words
    words = text.split()

    # Count word frequencies
    word_counts = pd.Series(words).value_counts()

    return word_counts