
import re
from nltk.corpus import stopwords

def task_func(text: str) -> dict:
    # Remove duplicate words and stopwords
    text = re.sub(r'\b\w+\b', '', text)
    stop_words = set(stopwords.words('english'))
    text = [word for word in text.split() if word not in stop_words]

    # Create a frequency distribution of the remaining words
    word_freq = {}
    for word in text:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    return word_freq