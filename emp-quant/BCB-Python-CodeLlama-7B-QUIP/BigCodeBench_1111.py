
from collections import Counter
from operator import itemgetter
import itertools
#CONSTANT
ANIMAL = ['cat', 'camel', 'cow', 'dog', 'elephant', 'fox', 'giraffe', 'hippo', 'iguana', 'jaguar']
def task_func(animal_dict):
    # Remove keys that are not in ANIMAL constant
    animal_dict = {k: v for k, v in animal_dict.items() if k in ANIMAL}
    # Count the frequency of each letter in the animals
    letter_freq = Counter(itertools.chain.from_iterable(animal_dict.values()))
    # Sort the frequencies in descending order
    sorted_freq = sorted(letter_freq.items(), key=itemgetter(1), reverse=True)
    return {k: v for k, v in sorted_freq}