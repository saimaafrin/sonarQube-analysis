from nltk.tokenize import RegexpTokenizer
from string import punctuation
import csv
import os
PUNCTUATION = set(punctuation)
def task_func(text, filename):
    """
    Save all words in a text beginning with the "$" character in a CSV file, excluding any words that are solely composed of punctuation characters.
    Note that:
    - The header of the csv row is "Word"
    - The function should output with:
        str: The absolute path of the saved CSV file.
    """
    # Tokenize the text into individual words
    tokenizer = RegexpTokenizer(r'\w+')
    words = tokenizer.tokenize(text)

    # Filter out words that are solely composed of punctuation characters
    words = [word for word in words if not set(word).issubset(PUNCTUATION)]

    # Save the filtered words to a CSV file
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Word'])
        for word in words:
            writer.writerow([word])

    # Return the absolute path of the saved CSV file
    return os.path.abspath(filename)
text = "This is a test text with some $words and punctuation."
filename = 'words.csv'