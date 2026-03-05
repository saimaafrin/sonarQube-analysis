from collections import Counter
from operator import itemgetter
import itertools
ANIMAL = ['cat', 'camel', 'cow', 'dog', 'elephant', 'fox', 'giraffe', 'hippo', 'iguana', 'jaguar']
def task_func(animal_dict):
    """
    Given a dictionary of animals as keys and letters as values, count the frequency of each letter in the animals.
    Remove key in the dictionary if it is not an animal from ANIMAL constant.
    Output with:
        dict: A dictionary with letters as keys and their frequencies as values, sorted in descending order by frequency. Format: {letter: frequency}.
    """
    # Remove keys that are not in the ANIMAL constant
    animal_dict = {key: value for key, value in animal_dict.items() if key in ANIMAL}

    # Count the frequency of each letter in the animals
    letter_freq = Counter()
    for animal in animal_dict.values():
        for letter in animal:
            letter_freq[letter] += 1

    # Sort the dictionary by frequency in descending order
    sorted_letter_freq = sorted(letter_freq.items(), key=itemgetter(1), reverse=True)

    return {letter: frequency for letter, frequency in sorted_letter_freq}