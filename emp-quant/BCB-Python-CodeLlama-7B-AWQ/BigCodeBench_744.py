import nltk
from string import punctuation
import pandas as pd
def task_func(text):
    """
    Finds all words in a text, that are separated by whitespace, beginning with the "$" character and computes their number of occurences.
    """
    if not isinstance(text, str):
        raise ValueError("text must be a string")

    # Tokenize the text into individual words
    tokens = nltk.word_tokenize(text)

    # Filter out words that are entirely made up of punctuation
    tokens = [token for token in tokens if token.isalpha()]

    # Filter out words that do not start with "$"
    tokens = [token for token in tokens if token.startswith("$")]

    # Count the frequency of each word
    word_freq = {}
    for token in tokens:
        if token not in word_freq:
            word_freq[token] = 1
        else:
            word_freq[token] += 1

    # Create a DataFrame with the results
    df = pd.DataFrame(word_freq.items(), columns=["Word", "Frequency"])

    return df
text = "$hello this i$s a $test $test $test"