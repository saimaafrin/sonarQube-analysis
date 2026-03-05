
from nltk.tokenize import RegexpTokenizer
from string import punctuation
import os

def task_func(text, output_filename):
    # Create a tokenizer that matches words starting with '$'
    tokenizer = RegexpTokenizer(r'\$[^\s]+')
    
    # Tokenize the input text
    tokens = tokenizer.tokenize(text)
    
    # Filter out tokens that are solely composed of punctuation characters
    filtered_tokens = [token for token in tokens if not all(char in punctuation for char in token)]
    
    # Write the filtered tokens to the output file
    with open(output_filename, 'w') as file:
        for token in filtered_tokens:
            file.write(token + '\n')
    
    # Return the absolute path to the output file
    return os.path.abspath(output_filename)