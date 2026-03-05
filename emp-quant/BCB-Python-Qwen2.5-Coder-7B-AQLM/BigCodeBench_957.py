
import string
import re

def task_func(text: str) -> tuple:
    # Remove special characters and whitespace
    cleaned_text = re.sub(r'[^\w\s]', '', text)
    
    # Split the text into words
    words = cleaned_text.split()
    
    # Count the number of words
    num_words = len(words)
    
    # Count the number of characters (excluding whitespace)
    num_characters = len(''.join(words))
    
    # Count the number of unique characters (excluding whitespace)
    unique_characters = len(set(''.join(words)))
    
    return (num_words, num_characters, unique_characters)