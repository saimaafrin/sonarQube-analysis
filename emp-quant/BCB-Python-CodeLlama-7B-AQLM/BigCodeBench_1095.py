from nltk.tokenize import RegexpTokenizer
from string import punctuation
import os
def task_func(text, output_filename):
    """
    Extracts words from the input text that begin with the '$' character and saves them to a specified file,
    excluding any words that are solely composed of punctuation characters.

    This function is useful for processing texts where '$' is used to denote special terms or entities and saves
    these terms to a file for further analysis or usage.

    Parameters:
    input_text (str): The text from which to extract '$' prefixed words.
    output_filename (str): The filename for the output file where the extracted words will be saved.

    Returns:
    str: The absolute path to the output file containing the '$' prefixed words.

    Requirements:
    - nltk.tokenize.RegexpTokenizer
    - string.punctuation
    - os

    Example:
    >>> example_text = "$example $valid $!invalid $$ alsoInvalid"
    >>> task_func(example_text, 'extracted_dollar_words.txt')
    '/absolute/path/to/extracted_dollar_words.txt'
    """
    # Create a tokenizer that will split the input text into words
    tokenizer = RegexpTokenizer(r'\w+')

    # Split the input text into words
    words = tokenizer.tokenize(text)

    # Create a list to store the extracted words
    extracted_words = []

    # Iterate over the words
    for word in words:
        # If the word begins with '$' and is not solely composed of punctuation characters, add it to the list
        if word.startswith('$') and not word.isalpha() and not word.isdigit():
            extracted_words.append(word)

    # Create a file to store the extracted words
    with open(output_filename, 'w') as f:
        # Iterate over the extracted words
        for word in extracted_words:
            # Write the word to the file
            f.write(word + '\n')

    # Return the absolute path to the output file
    return os.path.abspath(output_filename)