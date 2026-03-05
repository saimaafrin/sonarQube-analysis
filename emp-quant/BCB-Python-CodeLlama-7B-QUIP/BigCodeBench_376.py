
import nltk
import re
from collections import Counter
# Constants
STOPWORDS = nltk.corpus.stopwords.words('english')
def task_func(text):
    # Split the text into words
    words = nltk.word_tokenize(text)
    # Convert to lowercase
    words = [word.lower() for word in words]
    # Remove punctuation marks
    words = [re.sub(r'[^\w\s]', '', word) for word in words]
    # Remove stopwords
    words = [word for word in words if word not in STOPWORDS]
    # Calculate the frequency of each word
    freq = Counter(words)
    return freq