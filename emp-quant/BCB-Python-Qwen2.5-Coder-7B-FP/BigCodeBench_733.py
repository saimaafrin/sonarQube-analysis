import re
import string
def task_func(content):
    # Define a set of stop words
    stop_words = set(["the", "and", "is", "in", "of", "to", "a", "that", "it", "with", "for", "on", "at", "by", "from", "this", "an", "as", "but", "or", "not", "if", "so", "because", "while", "how", "why", "where", "when", "who", "what", "which", "whom", "whose", "how", "why", "where", "when", "who", "what", "which", "whom", "whose"])
    
    # Remove punctuation from the content
    content = content.translate(str.maketrans('', '', string.punctuation))
    
    # Split the content into words
    words = content.split()
    
    # Remove the last word
    words = words[:-1]
    
    # Count the non-stop words
    count = sum(1 for word in words if word.lower() not in stop_words)
    
    return count