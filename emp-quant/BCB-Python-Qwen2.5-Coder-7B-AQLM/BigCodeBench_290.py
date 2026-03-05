
import nltk
nltk.download('stopwords')
from collections import Counter
import os
from nltk.corpus import stopwords

# Constants
STOPWORDS = set(stopwords.words('english'))

def task_func(directory_path):
    unique_words = set()
    
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    words = f.read().lower().split()
                    words = [word for word in words if word.isalpha() and word not in STOPWORDS]
                    unique_words.update(words)
    
    return len(unique_words)