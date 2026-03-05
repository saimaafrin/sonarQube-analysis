
import re
from collections import Counter
from nltk.corpus import stopwords

def task_func(text: str) -> dict:
    # Remove punctuation and convert to lowercase
    text = re.sub(r'[^\w\s]', '', text).lower()

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    text = ' '.join([word for word in text.split() if word not in stop_words])

    # Tokenize and count the words
    words = re.split(r'\W+', text)
    counts = Counter(words)

    # Return the dictionary of words and their counts
    return counts