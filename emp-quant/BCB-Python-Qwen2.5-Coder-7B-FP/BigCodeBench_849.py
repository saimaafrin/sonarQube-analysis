import re
from nltk.corpus import stopwords
from collections import Counter
STOPWORDS = set(stopwords.words('english'))
def task_func(input_string):
    # Split the input string into individual lines
    lines = input_string.split('\n')
    
    # Initialize an empty list to store words
    words = []
    
    # Iterate over each line
    for line in lines:
        # Remove non-alphabetic characters and convert to lowercase
        cleaned_line = re.sub(r'[^a-zA-Z\s]', '', line).lower()
        
        # Split the cleaned line into words
        line_words = cleaned_line.split()
        
        # Add words to the list, excluding stopwords
        words.extend([word for word in line_words if word not in STOPWORDS])
    
    # Count the frequency of each word using Counter
    word_count = Counter(words)
    
    return word_count