import os
from nltk import word_tokenize
def task_func(file_path='File.txt'):
    """
    Tokenizes a text file using the NLTK library.
    This function reads each line from the file, breaks it into words or punctuation, and stores the tokens in a list.
    """
    with open(file_path, 'r') as f:
        lines = f.readlines()
    tokens = []
    for line in lines:
        tokens.extend(word_tokenize(line))
    return tokens