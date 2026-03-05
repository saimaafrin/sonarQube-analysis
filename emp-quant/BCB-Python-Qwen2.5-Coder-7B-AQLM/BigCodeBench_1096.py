
from nltk.tokenize import RegexpTokenizer
from string import punctuation
import csv
import os
PUNCTUATION = set(punctuation)
def task_func(text, filename):
    tokenizer = RegexpTokenizer(r'\b\w+\b')
    words = tokenizer.tokenize(text)
    filtered_words = [word for word in words if word.startswith('$') and not all(char in PUNCTUATION for char in word)]
    csv_path = os.path.abspath(filename)
    with open(csv_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Word'])
        writer.writerows([[word] for word in filtered_words])
    return csv_path