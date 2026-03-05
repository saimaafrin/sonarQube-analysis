
from collections import defaultdict
import re

def task_func(word: str) -> dict:
    """
    Find the occurrences of each two-letter combination in the sanitized word, where only alphabetic characters are considered.

    Args:
        word (str): The sanitized word to search for two-letter combinations.

    Returns:
        dict: A dictionary with keys as two-letter combinations and values as their counts in the sanitized word.
    """
    # Create a regular expression pattern to match two-letter combinations
    pattern = r"[a-zA-Z]{2}"

    # Create a defaultdict to store the counts of each two-letter combination
    counts = defaultdict(int)

    # Iterate over the matches in the word
    for match in re.finditer(pattern, word):
        # Get the two-letter combination
        combination = match.group()

        # Increment the count for the combination
        counts[combination] += 1

    return counts