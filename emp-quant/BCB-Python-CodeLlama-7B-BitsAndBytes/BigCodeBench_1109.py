
import os
from nltk import word_tokenize

def task_func(file_path='File.txt'):
    # Open the file and read it line by line
    with open(file_path, 'r') as f:
        lines = f.readlines()

    # Tokenize each line and store the tokens in a list
    tokens = []
    for line in lines:
        tokens.extend(word_tokenize(line))

    # Return the list of tokens
    return tokens