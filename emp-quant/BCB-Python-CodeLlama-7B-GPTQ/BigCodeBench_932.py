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

    # Create a Counter object to count the frequency of each two-letter combination
    counter = Counter(word[i:i+2] for i in range(len(word)-1))

    # Find the most common two-letter combination and its frequency
    most_common = counter.most_common(1)[0]

    # Return a list containing the tuple of the most common two-letter combination and its frequency
    return [most_common]