
from collections import Counter
import re

def task_func(word: str) -> list:
    # Remove non-alphabetic characters and convert to lowercase
    cleaned_word = re.sub(r'[^a-zA-Z]', '', word).lower()
    
    # If the cleaned word has fewer than 2 letters, return an empty list
    if len(cleaned_word) < 2:
        return []
    
    # Generate all possible two-letter combinations
    combinations = [cleaned_word[i:i+2] for i in range(len(cleaned_word) - 1)]
    
    # Count the frequency of each combination
    counter = Counter(combinations)
    
    # Find the most common combination and its frequency
    most_common_combination, frequency = counter.most_common(1)[0]
    
    # Return the result as a list containing a single tuple
    return [(most_common_combination, frequency)]