
from nltk.tokenize import RegexpTokenizer
from string import punctuation
import csv
import os

PUNCTUATION = set(punctuation)

def task_func(text, filename):
    # Tokenize the text using NLTK's RegexpTokenizer
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text)

    # Filter out tokens that are solely composed of punctuation characters
    filtered_tokens = [token for token in tokens if not set(token).issubset(PUNCTUATION)]

    # Write the filtered tokens to a CSV file
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Word'])
        for token in filtered_tokens:
            writer.writerow([token])

    # Return the absolute path of the saved CSV file
    return os.path.abspath(filename)