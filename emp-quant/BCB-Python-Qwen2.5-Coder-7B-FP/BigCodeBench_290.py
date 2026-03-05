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
                content = file.read().lower()
                # Tokenize the content into words
                words = nltk.word_tokenize(content)
                # Filter out non-alphabetic words and stopwords
                filtered_words = [word for word in words if word.isalpha() and word not in STOPWORDS]
                # Add the filtered words to the set of unique words
                unique_words.update(filtered_words)
    
    # Return the count of unique words
    return len(unique_words)
directory_path = 'path/to/your/directory'