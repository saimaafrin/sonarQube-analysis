
import string
import re

def task_func(text: str) -> tuple:
    # Remove punctuation from the text
    text = re.sub(f"[{string.punctuation}]", "", text)
    
    # Split the text into words
    words = text.split()
    
    # Count the number of words
    num_words = len(words)
    
    # Count the number of characters excluding whitespace
    num_characters = sum(len(word) for word in words)
    
    # Count the number of unique characters
    unique_characters = len(set(text.replace(" ", "")))
    
    return (num_words, num_characters, unique_characters)