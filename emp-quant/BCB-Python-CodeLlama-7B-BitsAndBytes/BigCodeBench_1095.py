
from nltk.tokenize import RegexpTokenizer
from string import punctuation
import os

def task_func(text, output_filename):
    # Create a tokenizer object
    tokenizer = RegexpTokenizer(r'\w+')

    # Tokenize the input text
    tokens = tokenizer.tokenize(text)

    # Filter out tokens that are solely composed of punctuation characters
    filtered_tokens = [token for token in tokens if not all(char in punctuation for char in token)]

    # Save the filtered tokens to a file
    with open(output_filename, 'w') as f:
        for token in filtered_tokens:
            if token.startswith('$'):
                f.write(token + '\n')

    # Return the absolute path to the output file
    return os.path.abspath(output_filename)