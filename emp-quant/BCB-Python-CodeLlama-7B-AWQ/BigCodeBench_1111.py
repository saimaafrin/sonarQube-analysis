from collections import Counter
from operator import itemgetter
import itertools
ANIMAL = ['cat', 'camel', 'cow', 'dog', 'elephant', 'fox', 'giraffe', 'hippo', 'iguana', 'jaguar']
def task_func(animal_dict):
    """
    Given a dictionary of animals as keys and letters as values, count the frequency of each letter in the animals.
    Note that: Remove key in the dictionary if it is not an animal from ANIMAL constant
    The function should output with:
        dict: A dictionary with letters as keys and their frequencies as values, sorted in descending order by frequency. Format: {letter: frequency}.
    """
    # Remove keys that are not in the ANIMAL constant
    animal_dict = {k: v for k, v in animal_dict.items() if k in ANIMAL}
    # Count the frequency of each letter in the animals
    letter_freq = Counter(itertools.chain.from_iterable(animal_dict.values()))
    # Sort the dictionary by frequency in descending order
    letter_freq = sorted(letter_freq.items(), key=itemgetter(1), reverse=True)
    return letter_freq
animal_dict = {'cat': 'c', 'camel': 'c', 'cow': 'o', 'dog': 'd', 'elephant': 'e', 'fox': 'x', 'giraffe': 'g', 'hippo': 'h', 'iguana': 'i', 'jaguar': 'j'}