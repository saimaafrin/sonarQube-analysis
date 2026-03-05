from collections import defaultdict
import re
def task_func(word: str) -> dict:
    """
    Find the occurrences of each two-letter combination in the sanitized word, where only alphabetic characters are considered.
    The function should output with:
        collections.defaultdict: A dictionary with keys as two-letter combinations and values as their counts in the sanitized word.
    """
    # Create a regular expression pattern to match two-letter combinations
    pattern = r"[a-zA-Z]{2}"

    # Create a dictionary to store the counts of each two-letter combination
    counts = defaultdict(int)

    # Iterate over the matches of the regular expression pattern in the sanitized word
    for match in re.finditer(pattern, word):
        # Get the two-letter combination from the match
        combination = match.group()

        # Increment the count of the two-letter combination in the dictionary
        counts[combination] += 1

    # Return the dictionary with the counts of each two-letter combination
    return counts