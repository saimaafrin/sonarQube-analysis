from collections import Counter
import re
def task_func(word: str) -> list:
    # Remove non-alphabetic characters and convert to lowercase
    cleaned_word = re.sub(r'[^a-z]', '', word.lower())
    
    # Check if the cleaned word has fewer than 2 letters
    if len(cleaned_word) < 2:
        return []
    
    # Generate all two-letter combinations
    combinations = [cleaned_word[i:i+2] for i in range(len(cleaned_word) - 1)]
    
    # Count the frequency of each combination
    combination_counts = Counter(combinations)
    
    # Find the most common combination and its frequency
    most_common_combination, frequency = combination_counts.most_common(1)[0]
    
    # Return the result as a list containing a single tuple
    return [(most_common_combination, frequency)]