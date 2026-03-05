from collections import Counter
from operator import itemgetter
import itertools
ANIMAL = ['cat', 'camel', 'cow', 'dog', 'elephant', 'fox', 'giraffe', 'hippo', 'iguana', 'jaguar']
def task_func(animal_dict):
    # Remove key in the dictionary if it is not an animal from ANIMAL constant
    animal_dict = {key: value for key, value in animal_dict.items() if key in ANIMAL}
    # Count the frequency of each letter in the animals
    letter_freq = Counter(itertools.chain.from_iterable(animal_dict.values()))
    # Sort the dictionary by frequency in descending order
    letter_freq = sorted(letter_freq.items(), key=itemgetter(1), reverse=True)
    # Return the sorted dictionary
    return letter_freq
animal_dict = {'cat': 'c', 'camel': 'c', 'cow': 'c', 'dog': 'd', 'elephant': 'e', 'fox': 'f', 'giraffe': 'g', 'hippo': 'h', 'iguana': 'i', 'jaguar': 'j'}