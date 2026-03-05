import nltk
from string import punctuation
import pandas as pd
def task_func(text):
    """
    Finds all words in a text, that are separated by whitespace, beginning with the "$" character and computes their number of occurrences.
    """
    if not isinstance(text, str):
        raise ValueError("text must be a string")

    # Tokenize the text into individual words
    words = nltk.word_tokenize(text)

    # Filter out words that are entirely made up of punctuation
    words = [word for word in words if word.isalpha()]

    # Filter out words that do not start with "$"
    words = [word for word in words if word.startswith("$")]

    # Count the frequency of each word
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    # Create a DataFrame with the results
    df = pd.DataFrame(word_freq.items(), columns=["Word", "Frequency"])

    return df
text = "$hello this i$s a $test $test $test"