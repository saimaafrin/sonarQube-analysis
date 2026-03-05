import random
from collections import Counter
def task_func(strings: list) -> dict:
    """
    Analyzes a given list of strings for the occurrence of a specific pattern and counts the occurrences.
    :param strings: A list of strings to be analyzed.
    :return: A dictionary with results of string analysis showing counts of the pattern.
    """
    pattern = "pattern"
    counts = Counter()
    for string in strings:
        if pattern in string:
            counts[string] += 1
    return counts
strings = ["string1", "string2", "string3", "string4", "string5"]