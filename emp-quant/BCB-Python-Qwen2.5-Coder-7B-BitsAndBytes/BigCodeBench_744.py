
import nltk
from string import punctuation
import pandas as pd

# Ensure necessary NLTK data is downloaded
nltk.download('punkt')

def task_func(text):
    # Check if the input is a string
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    # Tokenize the text into words
    words = nltk.word_tokenize(text)
    
    # Filter words that start with '$' and are not entirely made up of punctuation
    filtered_words = [word for word in words if word.startswith('$') and any(char.isalpha() for char in word)]
    
    # Create a dictionary to count occurrences of each filtered word
    word_count = {}
    for word in filtered_words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    # Convert the dictionary to a pandas DataFrame
    df = pd.DataFrame(list(word_count.items()), columns=["Word", "Frequency"])
    
    return df