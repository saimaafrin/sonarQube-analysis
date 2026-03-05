from collections import defaultdict
import re
def task_func(word: str) -> dict:
    """
    Find the occurrences of each two-letter combination in the sanitized word, where only alphabetic characters are considered.
    The function should output with:
        collections.defaultdict: A dictionary with keys as two-letter combinations and values as their counts in the sanitized word.
    """
    sanitized_word = re.sub(r'[^a-zA-Z]', '', word)
    two_letter_combinations = defaultdict(int)
    for i in range(len(sanitized_word) - 1):
        two_letter_combinations[sanitized_word[i:i+2]] += 1
    return two_letter_combinations