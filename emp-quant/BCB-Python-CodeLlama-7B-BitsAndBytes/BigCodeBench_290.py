
import nltk
nltk.download('stopwords')
from collections import Counter
import os
from nltk.corpus import stopwords

# Constants
STOPWORDS = set(stopwords.words('english'))

def task_func(directory_path):
    # Initialize the counter
    counter = Counter()

    # Iterate over all files in the directory
    for filename in os.listdir(directory_path):
        # Check if the file is a '.txt' file
        if filename.endswith('.txt'):
            # Open the file and read its contents
            with open(os.path.join(directory_path, filename), 'r') as file:
                # Tokenize the text and remove stopwords
                tokens = nltk.word_tokenize(file.read())
                tokens = [token for token in tokens if token.lower() not in STOPWORDS]

                # Update the counter with the unique tokens
                counter.update(tokens)

    # Return the total count of unique non-stop words
    return len(counter)