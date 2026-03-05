
import nltk
from string import punctuation
import pandas as pd

def task_func(text):
    # Tokenize the text
    tokens = nltk.word_tokenize(text)

    # Remove punctuation from the tokens
    tokens = [word for word in tokens if word not in punctuation]

    # Add the '$' prefix to the tokens
    tokens = ['$' + word for word in tokens]

    # Create a DataFrame with the tokens and their frequencies
    df = pd.DataFrame({'Word': tokens, 'Frequency': [1] * len(tokens)})

    return df