from string import ascii_lowercase
import re
from collections import Counter
def task_func(string):
    """
    If a string occurs, divide it the last time "-" occurs and count the frequency of each lowercase letter in the prefix of the string.
    The function should output with:
        dict: A dictionary with the frequency of each lowercase letter.
    """
    # Find the last occurrence of "-" in the string
    last_hyphen_index = string.rfind('-')
    # If there is no hyphen, return an empty dictionary
    if last_hyphen_index == -1:
        return {}
    # Extract the prefix of the string before the last hyphen
    prefix = string[:last_hyphen_index]
    # Count the frequency of each lowercase letter in the prefix
    letter_counts = Counter(prefix)
    # Return the dictionary of letter frequencies
    return letter_counts