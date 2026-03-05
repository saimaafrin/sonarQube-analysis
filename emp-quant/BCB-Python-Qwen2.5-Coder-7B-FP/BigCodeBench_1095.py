from nltk.tokenize import RegexpTokenizer
from string import punctuation
import os
def task_func(text, output_filename):
    # Create a tokenizer that splits text into words using regular expressions
    tokenizer = RegexpTokenizer(r'\b\w+\b')
    words = tokenizer.tokenize(text)
    
    # Filter words that start with '$' and are not solely composed of punctuation
    filtered_words = [word for word in words if word.startswith('$') and not all(char in punctuation for char in word)]
    
    # Write the filtered words to the output file
    with open(output_filename, 'w') as file:
        for word in filtered_words:
            file.write(word + '\n')
    
    # Return the absolute path to the output file
    return os.path.abspath(output_filename)