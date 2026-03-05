from collections import defaultdict
import re
def task_func(word: str) -> dict:
    """
    Find the occurrences of each two-letter combination in the sanitized word, where only alphabetic characters are considered.
    The function should output with:
        collections.defaultdict: A dictionary with keys as two-letter combinations and values as their counts in the sanitized word.
    """
    # Sanitize the input word
    word = re.sub(r'[^a-zA-Z]', '', word)

    # Create a dictionary to store the counts
    counts = defaultdict(int)

    # Iterate over the word and count the occurrences of each two-letter combination
    for i in range(len(word) - 1):
        combination = word[i:i+2]
        counts[combination] += 1

    return counts