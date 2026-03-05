import re
from nltk.corpus import stopwords
def task_func(text: str) -> dict:
    """
    Analyzes a given text string by removing duplicate words and stopwords defined by nltk.corpus, and then returns a frequency distribution of the remaining words.
    """
    # Remove duplicate words
    text = re.sub(r'\b(\w+)\b', r'\1', text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    text = [word for word in text.split() if word.lower() not in stop_words]

    # Create a frequency distribution of the remaining words
    word_freq = {}
    for word in text:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    return word_freq