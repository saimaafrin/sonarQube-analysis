
import re
from nltk.corpus import stopwords
from collections import Counter
STOPWORDS = set(stopwords.words('english'))

def task_func(input_string):
    # Split the input string into individual lines
    lines = input_string.split('\n')
    
    # Initialize a Counter to store word frequencies
    word_counter = Counter()
    
    # Iterate over each line
    for line in lines:
        # Remove non-alphabetic characters and convert to lowercase
        cleaned_line = re.sub(r'[^a-zA-Z\s]', '', line).lower()
        
        # Split the line into words
        words = cleaned_line.split()
        
        # Filter out stopwords and update the word counter
        filtered_words = [word for word in words if word not in STOPWORDS]
        word_counter.update(filtered_words)
    
    # Return the dictionary of word frequencies
    return dict(word_counter)