
from nltk.tokenize import RegexpTokenizer
from string import punctuation
import os

def task_func(text, output_filename):
    # Create a tokenizer that splits on whitespace and punctuation
    tokenizer = RegexpTokenizer(r'\W+')

    # Tokenize the input text
    tokens = tokenizer.tokenize(text)

    # Create a set of punctuation characters
    punct_set = set(punctuation)

    # Filter out tokens that are solely composed of punctuation characters
    filtered_tokens = [token for token in tokens if not set(token) <= punct_set]

    # Join the filtered tokens back into a string
    filtered_text = ' '.join(filtered_tokens)

    # Write the filtered text to a file
    with open(output_filename, 'w') as f:
        f.write(filtered_text)

    # Return the absolute path to the output file
    return os.path.abspath(output_filename)