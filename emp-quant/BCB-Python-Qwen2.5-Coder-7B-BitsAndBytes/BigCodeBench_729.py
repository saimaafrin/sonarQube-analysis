
import pickle
import os
import random
import string

def task_func(strings, filename=None):
    if filename is None:
        filename = ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + '.pkl'
    
    # Save the list of strings to a pickle file
    with open(filename, 'wb') as f:
        pickle.dump(strings, f)
    
    # Read the list of strings back from the pickle file
    with open(filename, 'rb') as f:
        loaded_strings = pickle.load(f)
    
    # Remove the pickle file after loading
    os.remove(filename)
    
    return loaded_strings