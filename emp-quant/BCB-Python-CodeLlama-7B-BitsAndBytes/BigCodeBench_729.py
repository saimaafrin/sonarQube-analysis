
import pickle
import os
import random
import string

def task_func(strings, filename=None):
    # Save the list of random strings to a pickle file
    if filename is None:
        filename = 'random_strings.pickle'
    with open(filename, 'wb') as f:
        pickle.dump(strings, f)

    # Read the list of random strings from the pickle file
    with open(filename, 'rb') as f:
        loaded_strings = pickle.load(f)

    return loaded_strings

# Generate a list of random strings
strings = [random.choice(string.ascii_letters) for i in range(10)]

# Save the list of random strings to a pickle file
task_func(strings)

# Read the list of random strings from the pickle file
loaded_strings = task_func(strings)

# Print the loaded list of random strings
print(loaded_strings)