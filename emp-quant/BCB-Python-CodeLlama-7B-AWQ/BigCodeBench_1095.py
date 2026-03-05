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

    # Tokenize the text
    tokens = tokenizer.tokenize(text)

    # Create a set to store the '$' prefixed words
    words = set()

    # Iterate over the tokens and check if they start with '$'
    for token in tokens:
        if token.startswith('$') and not token.isalpha():
            words.add(token)

    # Write the words to the output file
    with open(output_filename, 'w') as f:
        for word in words:
            f.write(word + '\n')

    # Return the absolute path to the output file
    return os.path.abspath(output_filename)
text = "This is a $test text with $special $terms and $punctuation."
output_filename = 'output.txt'