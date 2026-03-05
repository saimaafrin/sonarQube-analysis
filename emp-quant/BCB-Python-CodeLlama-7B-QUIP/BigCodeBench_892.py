
import random
from collections import Counter

def task_func(strings: list) -> dict:
    """
    Analyzes a given list of strings for the occurrence of a specific pattern and counts the occurrences.
    :param strings: A list of strings to be analyzed
    :return: A dictionary with results of string analysis showing counts of the pattern
    """
    pattern = "random"
    counts = Counter(pattern in s for s in strings)
    return {"pattern_counts": counts}