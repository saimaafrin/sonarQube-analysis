
from collections import Counter
import re

def task_func(word: str) -> list:
    # Remove non-alphabetic characters and convert to lowercase
    cleaned_word = re.sub(r'[^a-z]', '', word).lower()
    
    # Check if the cleaned word has fewer than 2 letters
    if len(cleaned_word) < 2:
        return []
    
    # Generate all two-letter combinations
    two_letter_combinations = [cleaned_word[i:i+2] for i in range(len(cleaned_word) - 1)]
    
    # Count the frequency of each two-letter combination
    combination_counts = Counter(two_letter_combinations)
    
    # Find the most common two-letter combination
    most_common_combination = combination_counts.most_common(1)
    
    return most_common_combination