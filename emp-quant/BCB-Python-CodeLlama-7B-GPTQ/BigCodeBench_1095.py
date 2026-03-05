from nltk.tokenize import RegexpTokenizer
from string import punctuation
import os
def task_func(text, output_filename):
    """
    Extracts words from the input text that begin with the '$' character and saves them to a specified file, excluding any words that are solely composed of punctuation characters.
    This function is useful for processing texts where '$' is used to denote special terms or entities and saves these terms to a file for further analysis or usage.
    """
    # Create a tokenizer object
    tokenizer = RegexpTokenizer(r'\w+')

    # Tokenize the input text
    tokens = tokenizer.tokenize(text)

    # Create a list to store the extracted words
    extracted_words = []

    # Iterate over the tokens and extract words that start with '$'
    for token in tokens:
        if token.startswith('$') and token.strip(punctuation) != '':
            extracted_words.append(token)

    # Write the extracted words to a file
    with open(output_filename, 'w') as f:
        f.write('\n'.join(extracted_words))

    # Return the absolute path to the output file
    return os.path.abspath(output_filename)
text = "This is a sample text with some $special terms and entities$."
output_filename = 'output.txt'