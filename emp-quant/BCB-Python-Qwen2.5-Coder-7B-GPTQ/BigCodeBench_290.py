import nltk
from collections import Counter
import os
from nltk.corpus import stopwords
STOPWORDS = set(stopwords.words('english'))
def task_func(directory_path):
    unique_words = set()
    
    # Iterate over all files in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory_path, filename)
            with open(file_path, 'r') as file:
                # Read the content of the file
                content = file.read()
                # Tokenize the content into words
                words = content.split()
                # Filter out non-stop words and add to the set
                for word in words:
                    if word.lower() not in STOPWORDS:
                        unique_words.add(word.lower())
    
    # Return the count of unique non-stop words
    return len(unique_words)