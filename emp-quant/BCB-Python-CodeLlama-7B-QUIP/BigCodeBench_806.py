
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from collections import Counter
# Constants
STOPWORDS = set(stopwords.words('english'))
def task_func(text, n=2):
    # Remove stopwords
    text = re.sub(r'\b' + '|'.join(STOPWORDS) + r'\b', '', text)
    # Tokenize and n-gram
    tokens = nltk.word_tokenize(text)
    ngrams = nltk.ngrams(tokens, n)
    # Count n-grams
    counts = Counter(ngrams)
    return counts