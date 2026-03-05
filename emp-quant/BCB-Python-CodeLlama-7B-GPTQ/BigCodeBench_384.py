import collections
import random
import itertools
ANIMALS = ['Cat', 'Dog', 'Elephant', 'Lion', 'Tiger', 'Bear', 'Giraffe', 'Horse', 'Rabbit', 'Snake', 'Zebra']
def task_func(animal_dict, max_count=10, seed=0):
    """
    Given a constant list of animals in ANIMALS, and a dictionary 'animal_dict' with keys as people's names and values as their favorite animal names, reverse the keys and values in a given dictionary and count the occurrences of each predefined animal name with a random count. Return the reversed dictionary and the counter with animal name occurrences. This function performs two tasks: 1. It reverses the given dictionary (animal_dict) such that the original values become keys and the original keys become lists of values. 2. It counts the occurrences of each animal name in a predefined list (ANIMALS). The count of each animal name is a random integer between 1 and max_count (inclusive).
    """
    # Reverse the keys and values in the given dictionary
    reversed_dict = {value: key for key, value in animal_dict.items()}

    # Count the occurrences of each animal name in the predefined list
    counter = collections.Counter()
    for animal in ANIMALS:
        counter[animal] = random.randint(1, max_count)

    return reversed_dict, counter
animal_dict = {'Alice': 'Cat', 'Bob': 'Dog', 'Charlie': 'Elephant', 'David': 'Lion', 'Eve': 'Tiger', 'Frank': 'Bear', 'Grace': 'Giraffe', 'Henry': 'Horse', 'Iris': 'Rabbit', 'Jane': 'Snake', 'Kate': 'Zebra'}