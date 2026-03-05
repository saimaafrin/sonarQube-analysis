
import nltk
nltk.download('stopwords')
from collections import Counter
import os
from nltk.corpus import stopwords

# Constants
STOPWORDS = set(stopwords.words('english'))

def task_func(directory_path):
    unique_words = set()
    
    for filename in os.listdir(directory_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory_path, filename)
            with open(file_path, 'r') as file:
                words = file.read().lower().split()
                words = [word for word in words if word.isalpha() and word not in STOPWORDS]
                unique_words.update(words)
    
    return len(unique_words)