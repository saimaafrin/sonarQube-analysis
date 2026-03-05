
import string
import re

def task_func(text: str) -> tuple:
    # Remove special characters and whitespace
    cleaned_text = re.sub(r'[^\w\s]', '', text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    
    # Split the text into words
    words = cleaned_text.split()
    
    # Count the number of words
    num_words = len(words)
    
    # Count the number of characters (excluding whitespace)
    num_characters = len(cleaned_text.replace(' ', ''))
    
    # Count the number of unique characters (excluding whitespace and special characters)
    unique_characters = len(set(cleaned_text.replace(' ', '').replace(string.punctuation, '')))
    
    return (num_words, num_characters, unique_characters)