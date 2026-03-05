from collections import Counter
import re
def task_func(word: str) -> list:
    """
    Finds the most common two-letter combination in a given, cleaned word (lowercased and alphabetic characters only) and returns its frequency.
    The search is case-insensitive and ignores non-alphabetic characters.
    The function should output with:
        list: A list containing a single tuple. The tuple consists of the most frequent two-letter combination (str)
        and its frequency (int). Returns an empty list if the word has fewer than 2 letters, or after cleaning,
        the word has fewer than 2 alphabetic characters.
    """
    # Clean the word by removing non-alphabetic characters and converting to lowercase
    word = re.sub(r'[^a-zA-Z]', '', word).lower()

    # Check if the word has fewer than 2 letters or fewer than 2 alphabetic characters
    if len(word) < 2 or len(re.findall(r'[a-zA-Z]', word)) < 2:
        return []

    # Create a Counter object to count the frequency of each two-letter combination
    counter = Counter(word[i:i+2] for i in range(len(word) - 1))

    # Return the most common two-letter combination and its frequency
    return [max(counter.items(), key=lambda x: x[1])]