
import collections
import random
import itertools

ANIMALS = ['Cat', 'Dog', 'Elephant', 'Lion', 'Tiger', 'Bear', 'Giraffe', 'Horse', 'Rabbit', 'Snake', 'Zebra']

def task_func(animal_dict, max_count=10, seed=0):
    random.seed(seed)
    reversed_dict = collections.defaultdict(list)
    animal_counter = collections.Counter()

    for person, animal in animal_dict.items():
        reversed_dict[animal].append(person)
        animal_counter[animal] += random.randint(1, max_count)

    return (reversed_dict, animal_counter)

result = task_func(animal_dict)
print(result)