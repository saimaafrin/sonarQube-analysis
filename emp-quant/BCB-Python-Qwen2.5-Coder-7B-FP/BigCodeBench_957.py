import string
import re
def task_func(text: str) -> tuple:
    # Remove special characters and convert to lowercase
    cleaned_text = re.sub(f"[{string.punctuation}]", "", text).lower()
    
    # Split the text into words
    words = cleaned_text.split()
    
    # Count the number of words
    num_words = len(words)
    
    # Count the number of characters (excluding whitespace)
    num_characters = len(cleaned_text.replace(" ", ""))
    
    # Count the number of unique characters
    unique_characters = len(set(cleaned_text.replace(" ", "")))
    
    return (num_words, num_characters, unique_characters)