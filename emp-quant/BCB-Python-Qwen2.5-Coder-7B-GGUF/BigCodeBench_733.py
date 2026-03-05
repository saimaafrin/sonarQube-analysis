
import re
import string

def task_func(content):
    # Define a set of stop words
    stop_words = set(["the", "and", "is", "in", "of", "to", "a", "an"])
    
    # Remove punctuation from the content
    content = content.translate(str.maketrans('', '', string.punctuation))
    
    # Split the content into words
    words = content.split()
    
    # Exclude the last word
    words = words[:-1]
    
    # Count non-stop words
    count = sum(1 for word in words if word.lower() not in stop_words)
    
    return count