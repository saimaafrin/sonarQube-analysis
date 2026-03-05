
import nltk
from string import punctuation
import pandas as pd

def task_func(text):
    if not isinstance(text, str):
        raise ValueError("Input text must be a string")
    
    # Tokenize the text into words
    words = nltk.word_tokenize(text)
    
    # Filter words that start with '$' and are not entirely made of punctuation
    filtered_words = [word for word in words if word.startswith('$') and not all(char in punctuation for char in word[1:])]
    
    # Count the occurrences of each filtered word
    word_counts = pd.Series(filtered_words).value_counts()
    
    # Create a DataFrame with the word and its frequency
    result_df = pd.DataFrame({'Word': word_counts.index, 'Frequency': word_counts.values})
    
    return result_df