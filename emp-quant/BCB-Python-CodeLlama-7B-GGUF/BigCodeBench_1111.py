
from collections import Counter
from operator import itemgetter
import itertools
#CONSTANT
ANIMAL = ['cat', 'camel', 'cow', 'dog', 'elephant', 'fox', 'giraffe', 'hippo', 'iguana', 'jaguar']
def task_func(animal_dict):
    # Remove non-animal keys
    animal_dict = {k: v for k, v in animal_dict.items() if k in ANIMAL}
    # Count frequencies
    freq_dict = Counter(itertools.chain.from_iterable(animal_dict.values()))
    # Sort by frequency
    sorted_freq_dict = sorted(freq_dict.items(), key=itemgetter(1), reverse=True)
    # Format output
    return {k: v for k, v in sorted_freq_dict}