
import os
from nltk import word_tokenize

def task_func(file_path='File.txt'):
    tokens = []
    with open(file_path, 'r') as file:
        for line in file:
            tokens.extend(word_tokenize(line))
    return tokens