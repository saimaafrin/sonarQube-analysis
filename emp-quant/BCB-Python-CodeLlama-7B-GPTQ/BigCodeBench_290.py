import nltk
from collections import Counter
import os
from nltk.corpus import stopwords
STOPWORDS = set(stopwords.words('english'))
def task_func(directory_path):
    """
    Count the number of unique non-stop words across all '.txt' files in a specified directory.
    """
    # Initialize the counter
    counter = Counter()

    # Iterate over all files in the directory
    for filename in os.listdir(directory_path):
        # Check if the file is a '.txt' file
        if filename.endswith('.txt'):
            # Open the file and read its contents
            with open(os.path.join(directory_path, filename), 'r') as f:
                contents = f.read()

            # Tokenize the contents and remove stopwords
            tokens = nltk.word_tokenize(contents)
            tokens = [token for token in tokens if token.lower() not in STOPWORDS]

            # Increment the counter for each unique token
            counter.update(tokens)

    # Return the total count of unique non-stop words
    return len(counter)
directory_path = 'path/to/directory'