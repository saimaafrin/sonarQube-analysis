
from nltk.tokenize import RegexpTokenizer
from string import punctuation
import csv
import os

PUNCTUATION = set(punctuation)

def task_func(text, filename):
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text)
    words = [token for token in tokens if token not in PUNCTUATION]
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Word'])
        writer.writerows(words)
    return os.path.abspath(filename)