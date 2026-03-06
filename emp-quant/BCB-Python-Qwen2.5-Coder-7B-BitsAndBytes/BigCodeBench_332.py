
import re
from collections import Counter
from nltk.corpus import stopwords

# Ensure the NLTK stopword corpus is downloaded
import nltk
nltk.download('stopwords')

def task_func(text: str) -> dict:
    # Tokenize the text using regex
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Get the set of English stop words
    stop_words = set(stopwords.words('english'))
    
    # Filter out stop words and count the remaining words
    filtered_words = [word for word in words if word not in stop_words]
    word_count = Counter(filtered_words)
    
    return dict(word_count)