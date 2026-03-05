
import re
from nltk.corpus import stopwords
def task_func(text: str) -> dict:
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = re.split(r'\W+', text.lower())
    words = [word for word in words if word not in stop_words]
    # Remove duplicate words
    words = sorted(set(words))
    # Create frequency distribution
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq