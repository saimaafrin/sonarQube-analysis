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
    text = [word for word in text.split() if word not in stop_words]

    # Create a frequency distribution of the remaining words
    freq_dist = {}
    for word in text:
        if word in freq_dist:
            freq_dist[word] += 1
        else:
            freq_dist[word] = 1

    return freq_dist