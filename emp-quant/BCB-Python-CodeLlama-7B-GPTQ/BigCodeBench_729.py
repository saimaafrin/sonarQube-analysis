import pickle
import os
import random
import string
def task_func(strings, filename=None):
    """
    Save the list of random strings "Strings" in a pickle file and then read it back for validation. If a filename is not provided, a unique filename is generated.
    The function should output with:
        loaded_strings (list): The loaded list of strings from the pickle file.
    """
    if filename is None:
        filename = f"{random.choice(string.ascii_letters)}{random.randint(1000, 9999)}.pickle"
    with open(filename, "wb") as f:
        pickle.dump(strings, f)
    with open(filename, "rb") as f:
        loaded_strings = pickle.load(f)
    return loaded_strings
strings = ["apple", "banana", "cherry"]
filename = "test.pickle"