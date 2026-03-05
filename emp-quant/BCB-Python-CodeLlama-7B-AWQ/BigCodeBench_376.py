import nltk
import re
from collections import Counter
STOPWORDS = nltk.corpus.stopwords.words('english')
def task_func(text):
    """
    Calculate the frequency of continuous words in a text string.
    The function splits the text into words, converts them to lowercase, removes punctuation marks and common stopwords (provided as a constant), and then calculates the frequency of each word.
    The function should output with:
        dict: A dictionary with words as keys and their frequencies as values.
    """
    # Remove punctuation marks and common stopwords
    text = re.sub(r'[^\w\s]', '', text)
    text = [word for word in text.split() if word.lower() not in STOPWORDS]
    # Calculate word frequencies
    word_freq = Counter(text)
    # Return dictionary with words as keys and their frequencies as values
    return word_freq
text = "This is a sample text with some words repeated."