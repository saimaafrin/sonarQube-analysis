
import re
import string

# Constants
PUNCTUATION = string.punctuation

def task_func(text):
    # Split the text into words
    words = re.findall(r'\b\w+\b', text)
    word_count = len(words)
    
    # Count punctuation marks
    punctuation_count = sum(1 for char in text if char in PUNCTUATION)
    
    return (word_count, punctuation_count)