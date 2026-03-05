import collections
import random
import itertools
ANIMALS = ['Cat', 'Dog', 'Elephant', 'Lion', 'Tiger', 'Bear', 'Giraffe', 'Horse', 'Rabbit', 'Snake', 'Zebra']
def task_func(animal_dict, max_count=10, seed=0):
    # Set the seed for random number generation for reproducibility
    random.seed(seed)
    
    # Reverse the dictionary
    reversed_dict = collections.defaultdict(list)
    for person, animal in animal_dict.items():
        reversed_dict[animal].append(person)
    
    # Count occurrences of each animal name
    animal_counter = collections.Counter()
    for animal in ANIMALS:
        # Randomly assign a count between 1 and max_count
        animal_counter[animal] = random.randint(1, max_count)
    
    return (reversed_dict, animal_counter)
animal_dict = {
    'Alice': 'Cat',
    'Bob': 'Dog',
    'Charlie': 'Elephant',
    'David': 'Lion',
    'Eve': 'Tiger',
    'Frank': 'Bear',
    'Grace': 'Giraffe',
    'Hank': 'Horse',
    'Ivy': 'Rabbit',
    'Jack': 'Snake',
    'Katie': 'Zebra'
}