
import re
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
# Constants
SENTENCES = ['This is a sentence', 'Another sentence here', 'More sentences']
def task_func(s: str) -> np.ndarray:
    # Tokenize the string
    tokens = re.split(r'\W+', s)
    # Create a dictionary of word frequencies
    word_freq = {}
    for word in tokens:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    # Create a list of word frequencies
    word_freq_list = []
    for word in word_freq:
        word_freq_list.append(word_freq[word])
    # Create a numpy array from the list of word frequencies
    vectorized_string = np.array(word_freq_list)
    return vectorized_string