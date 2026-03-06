
import random
from collections import Counter

def task_func(strings: list) -> dict:
    """
    Analyzes a given list of strings for the occurrence of a specific pattern and counts the occurrences.

    Args:
        strings (list): A list of strings to analyze.

    Returns:
        dict: A dictionary with results of string analysis showing counts of the pattern.
    """
    pattern = "pattern"
    counts = Counter()
    for string in strings:
        if pattern in string:
            counts[pattern] += 1
    return counts