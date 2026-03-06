
from collections import Counter
import random
import itertools

def task_func(length, count, seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)

    # Generate a list of random strings with the specified length
    strings = [random.choice('abcd') for _ in range(count)]

    # Create a Counter object to store the frequency of each letter
    counter = Counter()

    # Iterate over the strings and increment the counter for each letter
    for string in strings:
        for letter in string:
            counter[letter] += 1

    # Print the counter
    print(counter)

# Call the function with the desired parameters
task_func(length=5, count=1000, seed=42)