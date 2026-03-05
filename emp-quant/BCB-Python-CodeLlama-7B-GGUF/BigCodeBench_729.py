
import pickle
import os
import random
import string

def task_func(strings, filename=None):
    if filename is None:
        filename = f"{random.randint(100000, 999999)}.pickle"
    with open(filename, "wb") as f:
        pickle.dump(strings, f)
    with open(filename, "rb") as f:
        loaded_strings = pickle.load(f)
    return loaded_strings