
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
    # Loop through all files in the directory
    for file_name in os.listdir(directory_path):
        # Open the file
        with open(os.path.join(directory_path, file_name), 'r') as file:
            # Tokenize the file
            tokens = nltk.word_tokenize(file.read())
            # Remove stopwords
            tokens = [word for word in tokens if word not in STOPWORDS]
            # Count the unique words
            counter.update(tokens)
    # Return the unique word count
    return counter.most_common(1)[0][1]