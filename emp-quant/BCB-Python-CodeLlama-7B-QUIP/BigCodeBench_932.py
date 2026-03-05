
from collections import Counter
import re

def task_func(word: str) -> list:
    # Remove non-alphabetic characters
    word = re.sub(r'[^a-zA-Z]', '', word)
    # Convert to lowercase
    word = word.lower()
    # Split the word into individual characters
    word_list = list(word)
    # Create a Counter object for the word_list
    counter = Counter(word_list)
    # Get the most common two-letter combination
    most_common = counter.most_common(2)
    # Return an empty list if the word has fewer than 2 letters
    if len(most_common) < 2:
        return []
    # Return the most common two-letter combination and its frequency
    return [(most_common[0], most_common[1])]