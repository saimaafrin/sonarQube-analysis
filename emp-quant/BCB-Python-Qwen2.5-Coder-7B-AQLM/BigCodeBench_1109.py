
import os
from nltk import word_tokenize

def task_func(file_path='File.txt'):
    tokens = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            for line in file:
                tokens.extend(word_tokenize(line))
    else:
        print(f"The file {file_path} does not exist.")
    return tokens