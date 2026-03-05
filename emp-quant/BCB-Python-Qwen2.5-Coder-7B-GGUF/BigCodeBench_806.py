
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from collections import Counter

# Constants
STOPWORDS = set(stopwords.words('english'))

def task_func(text, n=2):
    # Remove non-alphabetic characters and convert to lowercase
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text).lower()
    
    # Tokenize the text
    tokens = cleaned_text.split()
    
    # Remove stopwords
    filtered_tokens = [token for token in tokens if token not in STOPWORDS]
    
    # Generate n-grams
    ngrams = [' '.join(filtered_tokens[i:i+n]) for i in range(len(filtered_tokens) - n + 1)]
    
    # Count the n-grams
    ngram_counts = Counter(ngrams)
    
    return ngram_counts