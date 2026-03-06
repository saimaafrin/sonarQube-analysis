
from collections import Counter
import itertools

def task_func(letters: list, repetitions: int) -> dict:
    # Repeat each letter in the list 'repetitions' times
    repeated_letters = list(itertools.chain.from_iterable([letter] * repetitions for letter in letters))
    
    # Count the frequency of each letter using Counter
    letter_frequency = Counter(repeated_letters)
    
    return letter_frequency