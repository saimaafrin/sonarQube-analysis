
import collections
import random
import itertools

ANIMALS = ['Cat', 'Dog', 'Elephant', 'Lion', 'Tiger', 'Bear', 'Giraffe', 'Horse', 'Rabbit', 'Snake', 'Zebra']

def task_func(animal_dict, max_count=10, seed=0):
    # Reverse the keys and values in the given dictionary
    reversed_dict = {value: key for key, value in animal_dict.items()}

    # Count the occurrences of each animal name in the predefined list
    animal_counts = collections.Counter()
    for animal in ANIMALS:
        animal_counts[animal] = random.randint(1, max_count)

    return reversed_dict, animal_counts