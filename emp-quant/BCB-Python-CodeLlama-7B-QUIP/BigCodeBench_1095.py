
from nltk.tokenize import RegexpTokenizer
from string import punctuation
import os

def task_func(text, output_filename):
    # Create a tokenizer that will only tokenize words that start with '$'
    tokenizer = RegexpTokenizer('[a-zA-Z0-9_]+')
    # Tokenize the input text
    tokens = tokenizer.tokenize(text)
    # Filter out any tokens that are solely composed of punctuation characters
    filtered_tokens = [token for token in tokens if token not in punctuation]
    # Filter out any tokens that do not start with '$'
    filtered_tokens = [token for token in filtered_tokens if token.startswith('$')]
    # Write the filtered tokens to a file
    with open(output_filename, 'w') as output_file:
        for token in filtered_tokens:
            output_file.write(token + '\n')
    # Return the absolute path to the output file
    return os.path.abspath(output_filename)