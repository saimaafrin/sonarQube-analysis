
from nltk.tokenize import RegexpTokenizer
from string import punctuation
import os

def task_func(text, output_filename):
    # Tokenize the text using a regular expression that matches words starting with '$'
    tokenizer = RegexpTokenizer(r'\b\$[a-zA-Z0-9]+\b')
    tokens = tokenizer.tokenize(text)
    
    # Filter out words that are solely composed of punctuation
    filtered_tokens = [token for token in tokens if token not in punctuation]
    
    # Write the filtered tokens to the output file
    with open(output_filename, 'w') as file:
        for token in filtered_tokens:
            file.write(token + '\n')
    
    # Return the absolute path to the output file
    return os.path.abspath(output_filename)