import nltk
from collections import Counter
import os
from nltk.corpus import stopwords
STOPWORDS = set(stopwords.words('english'))
def task_func(directory_path):
    """
    Counts the number of unique non-stop words across all '.txt' files in a specified directory.

    Args:
    directory_path (str): The path to the directory containing '.txt' files.

    Returns:
    int: The total count of unique non-stop words across all files.
    """
    unique_words = set()

    # Iterate over all files in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                # Read the content of the file
                content = file.read()
                # Tokenize the content into words
                words = nltk.word_tokenize(content)
                # Filter out stop words and add the remaining words to the set
                for word in words:
                    if word.isalpha() and word.lower() not in STOPWORDS:
                        unique_words.add(word.lower())

    # Return the count of unique non-stop words
    return len(unique_words)