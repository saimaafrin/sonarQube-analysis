from collections import Counter
import itertools
def task_func(letters: list, repetitions: int) -> dict:
    """
    Count the frequency of each letter in a list after repeating it a given number of times.
    Returns a dictionary where the keys are the letters and the values are their frequencies.
    """
    # Create a list of repeated letters
    repeated_letters = [letter for letter in letters for _ in range(repetitions)]

    # Count the frequency of each letter in the list
    letter_frequencies = Counter(repeated_letters)

    return letter_frequencies