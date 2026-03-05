
import re
import string

def task_func(content):
    # Define a set of stop words
    stop_words = set(["the", "and", "is", "in", "of", "that", "it", "with", "for", "on", "at", "to", "from", "by", "as", "but", "or", "not", "an", "a"])
    
    # Remove punctuation from the content
    content = content.translate(str.maketrans('', '', string.punctuation))
    
    # Split the content into words
    words = content.split()
    
    # Remove the last word
    words = words[:-1]
    
    # Count the non-stop words
    count = sum(1 for word in words if word.lower() not in stop_words)
    
    return count