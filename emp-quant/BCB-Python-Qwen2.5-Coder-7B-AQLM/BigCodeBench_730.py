
import pickle
import os
# Constants
FILE_NAME = 'save.pkl'

def task_func(dt):
    """
    Save the datetime object 'dt' in the pickle file 'save.pkl' and then read it back for validation.
    
    Args:
    dt (datetime): The datetime object to be saved.
    
    Returns:
    loaded_dt (datetime): The loaded datetime object from 'save.pkl'.
    """
    # Save the datetime object to a pickle file
    with open(FILE_NAME, 'wb') as file:
        pickle.dump(dt, file)
    
    # Read the datetime object back from the pickle file
    with open(FILE_NAME, 'rb') as file:
        loaded_dt = pickle.load(file)
    
    # Optionally, you can remove the file after loading
    os.remove(FILE_NAME)
    
    return loaded_dt