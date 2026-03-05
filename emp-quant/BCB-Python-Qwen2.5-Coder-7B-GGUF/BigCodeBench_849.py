
import re
from nltk.corpus import stopwords
from collections import Counter
STOPWORDS = set(stopwords.words('english'))

def task_func(input_string):
    # Split the input string into individual lines
    lines = input_string.split('\n')
    
    # Initialize an empty list to store all words
    all_words = []
    
    # Iterate over each line
    for line in lines:
        # Remove non-alphabetic characters and convert to lowercase
        cleaned_line = re.sub(r'[^a-zA-Z\s]', '', line).lower()
        # Split the line into words
        words = cleaned_line.split()
        # Filter out stopwords and add remaining words to the list
        filtered_words = [word for word in words if word not in STOPWORDS]
        all_words.extend(filtered_words)
    
    # Count the frequency of each word
    word_count = Counter(all_words)
    
    return word_count