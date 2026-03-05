from collections import Counter
import itertools
def task_func(letters: list, repetitions: int) -> dict:
    # Repeat each letter in the list the given number of times
    repeated_letters = itertools.chain.from_iterable(itertools.repeat(letter, repetitions) for letter in letters)
    # Count the frequency of each letter
    frequency = Counter(repeated_letters)
    return frequency