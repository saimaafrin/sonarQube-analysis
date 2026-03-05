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
    text = ' '.join([word for word in text.split() if word.lower() not in stop_words])

    # Count the frequency of each word
    word_counts = {}
    for word in text.split():
        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] += 1

    return word_counts