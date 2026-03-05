
import os
from nltk import word_tokenize

def task_func(file_path='File.txt'):
    with open(file_path, 'r') as f:
        text = f.read()
        tokens = word_tokenize(text)
    return tokens