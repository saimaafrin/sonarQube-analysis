
import re
from nltk.corpus import stopwords

def task_func(text: str) -> dict:
    # Remove duplicate words
    text = re.sub(r'\b(\w+)\b', r'\1', text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    text = ' '.join([word for word in text.split() if word.lower() not in stop_words])

    # Create frequency distribution
    word_freq = {}
    for word in text.split():
        if word not in word_freq:
            word_freq[word] = 1
        else:
            word_freq[word] += 1

    return word_freq