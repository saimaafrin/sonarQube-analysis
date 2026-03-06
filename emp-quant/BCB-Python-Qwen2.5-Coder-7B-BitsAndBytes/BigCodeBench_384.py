
import collections
import random
import itertools

ANIMALS = ['Cat', 'Dog', 'Elephant', 'Lion', 'Tiger', 'Bear', 'Giraffe', 'Horse', 'Rabbit', 'Snake', 'Zebra']

def task_func(animal_dict, max_count=10, seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Reverse the dictionary
    reversed_dict = {}
    for person, animal in animal_dict.items():
        if animal not in reversed_dict:
            reversed_dict[animal] = []
        reversed_dict[animal].append(person)
    
    # Count the occurrences of each animal name
    animal_counter = collections.Counter()
    for _ in range(max_count):
        for animal in ANIMALS:
            animal_counter[animal] += random.randint(1, max_count)
    
    return reversed_dict, animal_counter