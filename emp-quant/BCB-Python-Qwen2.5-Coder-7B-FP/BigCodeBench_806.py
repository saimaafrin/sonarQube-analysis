import re
import nltk
from nltk.corpus import stopwords
from collections import Counter
STOPWORDS = set(stopwords.words('english'))
def task_func(text, n=2):
    # Remove non-alphabetic characters and convert to lowercase
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text).lower()
    
    # Tokenize the text
    tokens = nltk.word_tokenize(cleaned_text)
    
    # Remove stopwords
    tokens = [token for token in tokens if token not in STOPWORDS]
    
    # Generate n-grams
    ngrams = list(nltk.ngrams(tokens, n))
    
    # Count the n-grams
    ngram_counts = Counter(ngrams)
    
    return ngram_counts