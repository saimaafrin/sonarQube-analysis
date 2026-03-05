from collections import defaultdict
import re
def task_func(word: str) -> dict:
    # Sanitize the word to keep only alphabetic characters
    sanitized_word = re.sub(r'[^a-zA-Z]', '', word)
    
    # Initialize a defaultdict to store the counts of two-letter combinations
    two_letter_counts = defaultdict(int)
    
    # Iterate over the sanitized word to count two-letter combinations
    for i in range(len(sanitized_word) - 1):
        two_letter = sanitized_word[i:i+2]
        two_letter_counts[two_letter] += 1
    
    return dict(two_letter_counts)