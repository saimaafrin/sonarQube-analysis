
from collections import Counter
from operator import itemgetter
import itertools

# CONSTANT
ANIMAL = ['cat', 'camel', 'cow', 'dog', 'elephant', 'fox', 'giraffe', 'hippo', 'iguana', 'jaguar']

def task_func(animal_dict):
    # Remove keys that are not in the ANIMAL constant
    animal_dict = {k: v for k, v in animal_dict.items() if k in ANIMAL}

    # Count the frequency of each letter in the animals
    letter_freq = Counter()
    for animal in animal_dict.values():
        letter_freq.update(animal)

    # Sort the dictionary by frequency in descending order
    sorted_freq = sorted(letter_freq.items(), key=itemgetter(1), reverse=True)

    # Return the sorted dictionary
    return {k: v for k, v in sorted_freq}