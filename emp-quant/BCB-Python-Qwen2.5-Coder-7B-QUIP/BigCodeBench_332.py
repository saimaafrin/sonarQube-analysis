
import re
from collections import Counter
from nltk.corpus import stopwords

def task_func(text: str) -> dict:
    # Initialize a set with common English stop words
    stop_words = set(stopwords.words('english'))
    
    # Use regular expression to find all words in the text
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Filter out stop words
    filtered_words = [word for word in words if word not in stop_words]
    
    # Count the occurrences of each non-stop word
    word_counts = Counter(filtered_words)
    
    return dict(word_counts)