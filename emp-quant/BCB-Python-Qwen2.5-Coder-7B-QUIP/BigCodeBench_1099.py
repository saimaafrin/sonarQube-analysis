
import re
from collections import Counter

# Predefined list of common stopwords
PREDEFINED_STOPWORDS = {
    "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", 
    "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", 
    "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", 
    "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", 
    "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", 
    "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", 
    "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", 
    "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", 
    "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "more"
}

def task_func(text):
    # Remove URLs from the text
    text = re.sub(r'http[s]?://[^\s]+', '', text)
    
    # Split the text into words
    words = text.split()
    
    # Filter out stopwords
    filtered_words = [word for word in words if word.lower() not in PREDEFINED_STOPWORDS]
    
    # Count the frequency of each word
    word_count = Counter(filtered_words)
    
    # Return the list of tuples with word and its frequency
    return list(word_count.items())