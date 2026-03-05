
import collections
import random
import itertools

ANIMALS = ['Cat', 'Dog', 'Elephant', 'Lion', 'Tiger', 'Bear', 'Giraffe', 'Horse', 'Rabbit', 'Snake', 'Zebra']

def task_func(animal_dict, max_count=10, seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)

    # Reverse the dictionary
    reversed_dict = collections.defaultdict(list)
    for key, value in animal_dict.items():
        reversed_dict[value].append(key)

    # Count the occurrences of each animal name
    animal_counter = collections.Counter()
    for _ in range(100):  # Assuming we want to count 100 times for each animal
        animal_name = random.choice(ANIMALS)
        animal_counter[animal_name] += 1

    # Return the reversed dictionary and the counter
    return (reversed_dict, animal_counter)