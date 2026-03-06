
import nltk
from string import punctuation
import pandas as pd

def task_func(text):
    if not isinstance(text, str):
        raise ValueError("text must be a string")

    # Tokenize the text into individual words
    tokens = nltk.word_tokenize(text)

    # Filter out any tokens that are entirely made up of punctuation
    tokens = [token for token in tokens if not all(char in punctuation for char in token)]

    # Filter out any tokens that do not start with '$'
    tokens = [token for token in tokens if token.startswith("$")]

    # Count the frequency of each token
    frequency = {token: tokens.count(token) for token in tokens}

    # Create a DataFrame with the results
    df = pd.DataFrame({"Word": tokens, "Frequency": frequency.values()})

    return df