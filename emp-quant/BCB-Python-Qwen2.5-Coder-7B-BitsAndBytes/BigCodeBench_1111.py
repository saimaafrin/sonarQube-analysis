
from collections import Counter
from operator import itemgetter
import itertools

# CONSTANT
ANIMAL = ['cat', 'camel', 'cow', 'dog', 'elephant', 'fox', 'giraffe', 'hippo', 'iguana', 'jaguar']

def task_func(animal_dict):
    # Filter out non-animal keys
    filtered_dict = {key: value for key, value in animal_dict.items() if key.lower() in ANIMAL}
    
    # Flatten the list of letters into a single string
    all_letters = ''.join(filtered_dict.values())
    
    # Count the frequency of each letter
    letter_count = Counter(all_letters)
    
    # Sort the dictionary by frequency in descending order
    sorted_letter_count = dict(sorted(letter_count.items(), key=itemgetter(1), reverse=True))
    
    return sorted_letter_count

result = task_func(animal_dict)
print(result)  # Output should be a sorted dictionary by frequency