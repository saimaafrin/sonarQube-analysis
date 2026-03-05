
import string
import re

def task_func(text: str) -> tuple:
    # Remove special characters and whitespace
    cleaned_text = re.sub(r'[^\w]', '', text)
    
    # Count the number of words
    words = cleaned_text.split()
    num_words = len(words)
    
    # Count the number of characters (excluding whitespace)
    num_characters = len(cleaned_text)
    
    # Count the number of unique characters
    unique_characters = len(set(cleaned_text))
    
    return (num_words, num_characters, unique_characters)