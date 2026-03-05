
from collections import Counter
import itertools

def task_func(letters: list, repetitions: int) -> dict:
    # Repeat the list of letters the given number of times
    repeated_letters = list(itertools.chain.from_iterable(itertools.repeat(letters, repetitions)))
    
    # Count the frequency of each letter in the repeated list
    letter_frequency = Counter(repeated_letters)
    
    # Return the dictionary of letter frequencies
    return letter_frequency