import re
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
def task_func(s: str) -> np.ndarray:
    """
    Vectorize a string using the Bag-of-Words model.
    The string is split into words and each word is treated as an attribute.
    The value of each attribute is the number of occurrences of the word in the string.
    The function also uses some predefined sentences (SENTENCES constant) for vectorization.
    """
    # Split the string into words
    words = re.split(r'\W+', s)
    # Create a dictionary of word frequencies
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    # Create a list of word frequencies
    word_freq_list = [word_freq[word] for word in words]
    # Create a numpy array with the vectorized string
    vectorized_string = np.array(word_freq_list)
    return vectorized_string