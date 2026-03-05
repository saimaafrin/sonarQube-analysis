
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from collections import Counter

# Constants
STOPWORDS = set(stopwords.words('english'))

def task_func(text, n=2):
    # Remove duplicate words
    words = text.split()
    words = list(set(words))
    
    # Remove stopwords
    words = [word for word in words if word not in STOPWORDS]
    
    # Generate n-grams
    n_grams = [words[i:i+n] for i in range(len(words)-n+1)]
    
    # Count n-grams
    n_gram_counts = Counter(n_grams)
    
    return dict(n_gram_counts)