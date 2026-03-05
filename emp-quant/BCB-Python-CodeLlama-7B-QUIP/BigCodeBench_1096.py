
from nltk.tokenize import RegexpTokenizer
from string import punctuation
import csv
import os

PUNCTUATION = set(punctuation)

def task_func(text, filename):
    # Create a tokenizer that will only keep words that start with the "$" character
    tokenizer = RegexpTokenizer(r"[a-zA-Z]+$")
    # Tokenize the text
    tokens = tokenizer.tokenize(text)
    # Remove any tokens that are solely composed of punctuation characters
    tokens = [t for t in tokens if t not in PUNCTUATION]
    # Create a list of words
    words = [t.strip() for t in tokens]
    # Write the words to a CSV file
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Word"])
        writer.writerows(words)
    return os.path.abspath(filename)