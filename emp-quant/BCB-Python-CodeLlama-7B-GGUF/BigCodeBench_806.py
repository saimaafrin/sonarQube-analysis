
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from collections import Counter
# Constants
STOPWORDS = set(stopwords.words('english'))
def task_func(text, n=2):
    # Remove stopwords and duplicates
    text = re.sub(r'\b(' + r'|'.join(STOPWORDS) + r')\b', '', text)
    text = re.sub(r'\b(\w+)\b', r'\1\1', text)
    # Generate n-grams
    ngrams = Counter()
    for i in range(len(text) - n + 1):
        ngrams[text[i:i+n]] += 1
    return ngrams