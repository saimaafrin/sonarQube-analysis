import pickle
import os
import random
import string
def task_func(strings, filename=None):
    if filename is None:
        filename = ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + '.pkl'
    
    # Save the list of strings to a pickle file
    with open(filename, 'wb') as file:
        pickle.dump(strings, file)
    
    # Read the list of strings back from the pickle file
    with open(filename, 'rb') as file:
        loaded_strings = pickle.load(file)
    
    # Remove the pickle file after reading
    os.remove(filename)
    
    return loaded_strings