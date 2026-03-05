
from collections import Counter
from operator import itemgetter
import itertools
#CONSTANT
ANIMAL = ['cat', 'camel', 'cow', 'dog', 'elephant', 'fox', 'giraffe', 'hippo', 'iguana', 'jaguar']

def task_func(animal_dict):
    # Filter out non-animal keys
    filtered_dict = {key: value for key, value in animal_dict.items() if key in ANIMAL}
    
    # Flatten the list of values (letters) and count their frequency
    flattened_values = list(itertools.chain.from_iterable(filtered_dict.values()))
    letter_counts = Counter(flattened_values)
    
    # Sort the letter counts in descending order
    sorted_letter_counts = sorted(letter_counts.items(), key=itemgetter(1), reverse=True)
    
    # Convert the sorted list of tuples back to a dictionary
    sorted_dict = dict(sorted_letter_counts)
    
    return sorted_dict