import re
import nltk
from nltk.corpus import stopwords
from collections import Counter
STOPWORDS = set(stopwords.words('english'))
def task_func(text, n=2):
    # Remove non-alphabetic characters and convert to lowercase
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text).lower()
    
    # Tokenize the text into words
    words = cleaned_text.split()
    
    # Remove stopwords
    words = [word for word in words if word not in STOPWORDS]
    
    # Generate n-grams
    ngrams = [' '.join(words[i:i+n]) for i in range(len(words) - n + 1)]
    
    # Count the n-grams
    ngram_counts = Counter(ngrams)
    
    return ngram_counts
text = "This is a sample text. This text is used for testing."