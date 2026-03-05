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
        # Remove punctuation and convert to lowercase
        cleaned_line = re.sub(r'[^\w\s]', '', line).lower()
        
        # Split the line into words and add to the list
        words.extend(cleaned_line.split())
    
    # Remove stopwords from the list of words
    filtered_words = [word for word in words if word not in STOPWORDS]
    
    # Count the frequency of each word using Counter
    word_frequency = Counter(filtered_words)
    
    return word_frequency