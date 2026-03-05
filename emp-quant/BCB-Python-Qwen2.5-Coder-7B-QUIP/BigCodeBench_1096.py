
from nltk.tokenize import RegexpTokenizer
from string import punctuation
import csv
import os
PUNCTUATION = set(punctuation)
def task_func(text, filename):
    tokenizer = RegexpTokenizer(r'\b\w+\b')
    words = tokenizer.tokenize(text)
    filtered_words = [word for word in words if word[0] == '$' and not all(char in PUNCTUATION for char in word)]
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Word'])
        writer.writerow(filtered_words)
    return os.path.abspath(filename)