
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
    tokens = nltk.word_tokenize(cleaned_text)
    
    # Remove stopwords
    filtered_tokens = [token for token in tokens if token not in STOPWORDS]
    
    # Generate n-grams
    n_grams = list(nltk.ngrams(filtered_tokens, n))
    
    # Count the n-grams
    n_gram_counts = Counter(n_grams)
    
    return n_gram_counts