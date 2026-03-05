
import nltk
import re
from collections import Counter

# Constants
STOPWORDS = nltk.corpus.stopwords.words('english')

def task_func(text):
    # Split text into words
    words = nltk.word_tokenize(text)

    # Convert words to lowercase
    words = [word.lower() for word in words]

    # Remove punctuation marks
    words = [re.sub(r'[^\w\s]', '', word) for word in words]

    # Remove common stopwords
    words = [word for word in words if word.lower() not in STOPWORDS]

    # Calculate frequency of each word
    word_freq = Counter(words)

    # Return dictionary with words as keys and frequencies as values
    return word_freq