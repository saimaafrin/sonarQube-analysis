
import nltk
nltk.download('stopwords')
from collections import Counter
import os
from nltk.corpus import stopwords

# Constants
STOPWORDS = set(stopwords.words('english'))

def task_func(directory_path):
    # Initialize a counter to keep track of word frequencies
    word_counter = Counter()
    
    # Walk through the directory and its subdirectories
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    text = f.read().lower()  # Read and convert text to lowercase
                    words = nltk.word_tokenize(text)  # Tokenize the text into words
                    filtered_words = [word for word in words if word.isalpha() and word not in STOPWORDS]  # Filter out non-alphabetic and stop words
                    word_counter.update(filtered_words)  # Update the counter with the filtered words
    
    # Return the total count of unique non-stop words
    return len(word_counter)