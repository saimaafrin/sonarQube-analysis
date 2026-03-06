
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from collections import Counter

# Constants
STOPWORDS = set(stopwords.words('english'))

def task_func(text, n=2):
    # Remove duplicate and stopwords from the text
    text = re.sub(r'\b\w+\b', ' ', text)
    text = ' '.join([word for word in text.split() if word.lower() not in STOPWORDS])

    # Generate count of n-grams
    ngrams = Counter(text.split())

    # Output the count of n-grams
    return ngrams