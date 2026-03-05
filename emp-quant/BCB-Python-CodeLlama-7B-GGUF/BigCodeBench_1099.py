
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
    # Remove URLs
    text = re.sub(r"http\S+", "", text)

    # Tokenize the text
    tokens = text.split()

    # Remove stopwords
    tokens = [token for token in tokens if token.lower() not in PREDEFINED_STOPWORDS]

    # Count the remaining tokens
    counts = Counter(tokens)

    # Return the list of tuples
    return counts.most_common()