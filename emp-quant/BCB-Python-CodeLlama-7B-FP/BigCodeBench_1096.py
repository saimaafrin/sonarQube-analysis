from nltk.tokenize import RegexpTokenizer
from string import punctuation
import csv
import os
PUNCTUATION = set(punctuation)
def task_func(text, filename):
    """
    Save all words in a text beginning with the "$" character in a CSV file, excluding any words that are solely composed of punctuation characters.
    """
    tokenizer = RegexpTokenizer(r'\w+')
    words = tokenizer.tokenize(text)
    words = [word for word in words if word[0] == '$' and not set(word).issubset(PUNCTUATION)]
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Word'])
        writer.writerows(words)
    return os.path.abspath(filename)