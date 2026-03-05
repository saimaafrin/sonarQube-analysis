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
    word_count = Counter()

    # Iterate over all files in the directory
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.txt'):
                # Open file and read contents
                with open(os.path.join(root, file), 'r') as f:
                    contents = f.read()

                # Tokenize contents and remove stopwords
                tokens = nltk.word_tokenize(contents)
                tokens = [word for word in tokens if word not in STOPWORDS]

                # Update counter
                word_count.update(tokens)

    # Return total count of unique non-stop words
    return len(word_count)
directory_path = 'path/to/directory'
tokens = nltk.word_tokenize(contents)
word_count = Counter(tokens)