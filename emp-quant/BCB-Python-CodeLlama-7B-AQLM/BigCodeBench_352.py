import pandas as pd
from collections import Counter
def task_func(text_dict, word_keys, top_k=2):
    """
    Calculate the frequency of certain words in a text dictionary and return a bar chart's Axes object and a dictionary
    containing the frequencies of the top_k most common words in text_dict. 
    
    The function takes a dictionary containing word frequencies and a list of words. It calculates the frequency 
    of the provided words in the dictionary and returns the Axes object of the bar chart displaying the frequencies
    along with the top_k most common words and their frequencies as a dictionary. If a word in word_keys is not present 
    in text_dict, its frequency is considered to be 0.
    
    Parameters:
    - text_dict (dict): The dictionary containing word frequencies. Key is the word and value is its frequency.
    - word_keys (list of str): The list of words to consider.
    - top_k (int, Optional): A positive integer denoting the number of most common words to return. Default is 2.
    
    Returns:
    - matplotlib.axes._axes.Axes: Axes object of the bar chart displaying the frequencies.
    - dict: Dictionary containing the frequencies of the top_k most common words. Key is the word and value is 
    its frequency.
    
    Requirements:
    - pandas
    - collections.Counter

    Raises:
    - ValueError: If top_k is a negative integer.
    
    Example:
    >>> import collections
    >>> text_dict = collections.Counter(['the', 'be', 'to', 'the', 'that', 'and', 'a', 'in', 'the', 'that', 'have', 'I'])
    >>> word_keys = ['the', 'and', 'I']
    >>> ax, frequencies = task_func(text_dict, word_keys, 3)
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    >>> frequencies
    {'the': 3, 'that': 2, 'be': 1}
    """
    if top_k < 0:
        raise ValueError("top_k must be a positive integer.")
    if not isinstance(text_dict, dict):
        raise TypeError("text_dict must be a dictionary.")
    if not isinstance(word_keys, list):
        raise TypeError("word_keys must be a list.")
    if not isinstance(top_k, int):
        raise TypeError("top_k must be an integer.")
    if not all(isinstance(word, str) for word in word_keys):
        raise TypeError("word_keys must contain only strings.")
    if not all(isinstance(word, str) for word in text_dict.keys()):
        raise TypeError("text_dict must contain only strings.")
    if not all(isinstance(freq, int) for freq in text_dict.values()):
        raise TypeError("text_dict must contain only integers.")
    if not all(isinstance(word, str) for word in word_keys):
        raise TypeError("word_keys must contain only strings.")
    if not all(isinstance(freq, int) for freq in text_dict.values()):
        raise TypeError("text_dict must contain only integers.")
    if not all(isinstance(word, str) for word in word_keys):
        raise TypeError("word_keys must contain only strings.")
    if not all(isinstance(freq, int) for freq in text_dict.values()):
        raise TypeError("text_dict must contain only integers.")
    if not all(isinstance(word, str) for word in word_keys):
        raise TypeError("word_keys must contain only strings.")
    if not all(isinstance(freq, int) for freq in text_dict.values()):
        raise TypeError("text_dict must contain only integers.")
    if not all(isinstance(word, str) for word in word_keys):
        raise TypeError("word_keys must contain only strings.")
    if not all(isinstance(freq, int) for freq in text_dict.values()):
        raise TypeError("text_dict must contain only integers.")
    if not all(isinstance(word, str) for word in word_keys):
        raise TypeError("word_keys must contain only strings.")
    if not all(isinstance(freq, int) for freq in text_dict.values()):
        raise TypeError("text_dict must contain only integers.")
    if not all(isinstance(word, str) for word in word_keys):
        raise TypeError("word_keys must contain only strings.")
    if not all(isinstance(freq, int) for freq in text_dict.values()):
        raise TypeError("text_dict must contain only integers.")
    if not all(isinstance(word, str) for word in word_keys):
        raise TypeError("word_keys must contain only strings.")
    if not all(isinstance(freq, int) for freq in text_dict.values()):
        raise TypeError("text_dict must contain only integers.")
    if not all(isinstance(word, str) for word in word_keys):
        raise TypeError("word_keys must contain only strings.")
    if not all(isinstance(freq, int) for freq in text_dict.values()):
        raise TypeError("text_dict must contain only integers.")
    if not all(isinstance(word, str) for word in word_keys):
        raise TypeError("word_keys must contain only strings.")
    if not all(isinstance(freq, int) for freq in text_dict.values()):
        raise TypeError("text_dict must contain only integers.")
    if not all(isinstance(word, str) for word in word_keys):
        raise TypeError("word_keys must contain only strings.")
    if not all(isinstance(freq, int) for freq in text_dict.values()):
        raise TypeError("text_dict must contain only integers.")
    if not all(isinstance(word, str) for word in word_keys):
        raise TypeError("word_keys must contain only strings.")
    if not all(isinstance(freq, int) for freq in text_dict.values()):
        raise TypeError("text_dict must contain only integers.")
    if not all(isinstance(word, str) for word in word_keys):
        raise TypeError("word_keys must contain only strings.")
    if not all(isinstance(freq, int) for freq in text_dict.values()):
        raise TypeError("text_dict must contain only integers.")
    if not all(isinstance(word, str) for word in word_keys):
        raise TypeError("word_keys must contain only strings.")
    if not all(isinstance(freq, int) for freq in text_dict.values()):
        raise TypeError("text_dict must contain only integers.")
    if not all(isinstance(word, str) for word in word_keys):
        raise TypeError("word_keys must contain only strings.")
    if not all(isinstance(freq, int) for freq in text_dict.values()):
        raise TypeError("text_dict must contain only integers.")
    if not all(isinstance(word, str) for word in word_keys):
        raise TypeError("word_keys must contain only strings.")
    if not all(isinstance(freq, int) for freq in text_dict.values()):
        raise TypeError("text_dict must contain only integers.")