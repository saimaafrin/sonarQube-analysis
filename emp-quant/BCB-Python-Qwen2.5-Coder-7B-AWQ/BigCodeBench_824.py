import re
import string
PUNCTUATION = string.punctuation
def task_func(text):
    # Initialize counters
    word_count = 0
    punctuation_count = 0
    
    # Split the text into words
    words = re.split(r'\s+', text)
    word_count = len(words)
    
    # Count punctuation marks
    for char in text:
        if char in PUNCTUATION:
            punctuation_count += 1
    
    return (word_count, punctuation_count)
text = "Hello, world! This is a test string with punctuation."