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
        # Use regular expression to find words and convert them to lowercase
        words.extend(re.findall(r'\b\w+\b', line.lower()))
    
    # Filter out stopwords
    words = [word for word in words if word not in STOPWORDS]
    
    # Count the frequency of each word using Counter
    word_frequency = Counter(words)
    
    return word_frequency