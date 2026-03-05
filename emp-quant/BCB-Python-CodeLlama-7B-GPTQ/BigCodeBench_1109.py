import os
from nltk import word_tokenize
def task_func(file_path='File.txt'):
    """
    Tokenizes a text file using the NLTK library.
    This function reads each line from the file, breaks it into words or punctuation, and stores the tokens in a list.
    The function should output with:
        list: A list of tokens.
    """
    # Open the file
    with open(file_path, 'r') as f:
        # Read each line
        lines = f.readlines()
        # Tokenize each line
        tokens = [word_tokenize(line) for line in lines]
        # Flatten the list of lists
        tokens = [item for sublist in tokens for item in sublist]
    return tokens