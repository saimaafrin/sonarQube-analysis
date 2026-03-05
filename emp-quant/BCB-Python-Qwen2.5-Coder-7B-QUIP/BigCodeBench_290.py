
import nltk
nltk.download('stopwords')
from collections import Counter
import os
from nltk.corpus import stopwords
# Constants
STOPWORDS = set(stopwords.words('english'))

def task_func(directory_path):
    # Initialize a Counter to keep track of unique non-stop words
    unique_non_stop_words = Counter()

    # Iterate over all files in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                # Read the content of the file and split it into words
                words = file.read().split()
                # Filter out stop words and add the remaining words to the Counter
                non_stop_words = [word for word in words if word.lower() not in STOPWORDS]
                unique_non_stop_words.update(non_stop_words)

    # Return the total count of unique non-stop words
    return len(unique_non_stop_words)