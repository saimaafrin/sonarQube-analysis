
import re
from collections import Counter
from nltk.corpus import stopwords

def task_func(text: str) -> dict:
    # Remove punctuation and convert to lowercase
    text = re.sub(r'[^\w\s]', '', text.lower())

    # Tokenize the text
    tokens = text.split()

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]

    # Count the number of non-stop words
    counts = Counter(tokens)

    # Return a dictionary with the words and their counts
    return dict(counts)