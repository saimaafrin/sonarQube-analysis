import nltk
from string import punctuation
import pandas as pd
def task_func(text):
    # Check if the input is a string
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    # Tokenize the text into words
    words = nltk.word_tokenize(text)
    
    # Filter words that start with '$' and are not entirely made up of punctuation
    filtered_words = [word for word in words if word.startswith('$') and not all(char in punctuation for char in word)]
    
    # Count the frequency of each filtered word
    word_counts = pd.Series(filtered_words).value_counts().reset_index()
    word_counts.columns = ['Word', 'Frequency']
    
    return word_counts
text = "$hello this i$s a $test $test $test"