
import re
from collections import Counter
from nltk.corpus import stopwords

def task_func(text: str) -> dict:
    # Download the stopwords if not already downloaded
    stopwords.download('english')
    
    # Normalize the text to lower case
    text = text.lower()
    
    # Use regular expression to find words
    words = re.findall(r'\b\w+\b', text)
    
    # Remove stopwords
    filtered_words = [word for word in words if word not in stopwords.words('english')]
    
    # Count the occurrences of each word
    word_counts = Counter(filtered_words)
    
    return dict(word_counts)