import nltk
from collections import Counter
import os
from nltk.corpus import stopwords
STOPWORDS = set(stopwords.words('english'))
def task_func(directory_path):
    """
    Count the number of unique non-stop words across all '.txt' files in a specified directory.
    """
    # Initialize counter
    counter = Counter()
    # Iterate over all files in the directory
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            # Check if the file is a '.txt' file
            if file.endswith('.txt'):
                # Open the file and read its contents
                with open(os.path.join(root, file), 'r') as f:
                    contents = f.read()
                # Tokenize the contents
                tokens = nltk.word_tokenize(contents)
                # Remove stopwords
                tokens = [token for token in tokens if token.lower() not in STOPWORDS]
                # Update the counter
                counter.update(tokens)
    # Return the total count of unique non-stop words
    return len(counter)
directory_path = 'path/to/directory'