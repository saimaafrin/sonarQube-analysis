from nltk.tokenize import RegexpTokenizer
from string import punctuation
import os
def task_func(text, output_filename):
    """
    Extracts words from the input text that begin with the '$' character and saves them to a specified file, excluding any words that are solely composed of punctuation characters.

    Args:
        text (str): The input text.
        output_filename (str): The name of the output file.

    Returns:
        str: The absolute path to the output file containing the '$' prefixed words.
    """
    # Create a tokenizer that splits the text into individual words
    tokenizer = RegexpTokenizer(r'\w+')

    # Tokenize the text and filter out any words that are solely composed of punctuation characters
    words = [word for word in tokenizer.tokenize(text) if word.isalpha() and word.startswith('$')]

    # Write the filtered words to a file
    with open(output_filename, 'w') as f:
        f.write('\n'.join(words))

    # Return the absolute path to the output file
    return os.path.abspath(output_filename)
text = "This is a sample text with some $special words and $entities."
output_filename = 'output.txt'