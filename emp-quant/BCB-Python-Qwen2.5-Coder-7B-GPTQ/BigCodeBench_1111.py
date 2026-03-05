from collections import Counter
from operator import itemgetter
import itertools
ANIMAL = ['cat', 'camel', 'cow', 'dog', 'elephant', 'fox', 'giraffe', 'hippo', 'iguana', 'jaguar']
def task_func(animal_dict):
    # Filter out non-animal keys
    filtered_dict = {key: value for key, value in animal_dict.items() if key in ANIMAL}
    
    # Flatten the list of letters and count the frequency
    letter_counts = Counter(itertools.chain.from_iterable(filtered_dict.values()))
    
    # Sort the dictionary by frequency in descending order
    sorted_letter_counts = dict(sorted(letter_counts.items(), key=itemgetter(1), reverse=True))
    
    return sorted_letter_counts
animal_dict = {
    'cat': 'catt',
    'camel': 'cammel',
    'cow': 'coww',
    'dog': 'dogg',
    'elephant': 'elephantt',
    'fox': 'fox',
    'giraffe': 'giraffee',
    'hippo': 'hippo',
    'iguana': 'iguanaa',
    'jaguar': 'jaguar',
    'bird': 'bird'  # This key will be removed as it's not in ANIMAL
}