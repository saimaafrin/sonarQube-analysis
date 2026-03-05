import nltk
import re
from collections import Counter
STOPWORDS = nltk.corpus.stopwords.words('english')
def task_func(text):
    # Tokenize the text into words
    words = re.findall(r'\b\w+\b', text.lower())
    # Remove stopwords
    words = [word for word in words if word not in STOPWORDS]
    # Count the frequency of each word
    word_freq = Counter(words)
    return word_freq
text = "Hello world! Hello everyone. Welcome to the world of Python."