
import pickle
import os
from datetime import datetime

# Constants
FILE_NAME = 'save.pkl'

def task_func(dt):
    """
    Save the datetime object 'dt' to a pickle file named 'save.pkl' and then load it back.

    Args:
        dt (datetime): The datetime object to be saved.

    Returns:
        loaded_dt (datetime): The loaded datetime object from 'save.pkl'.
    """
    # Save the datetime object to a pickle file
    with open(FILE_NAME, 'wb') as f:
        pickle.dump(dt, f)

    # Load the datetime object from the pickle file
    with open(FILE_NAME, 'rb') as f:
        loaded_dt = pickle.load(f)

    return loaded_dt

    # Call the function
    loaded_dt = task_func(sample_dt)
    
    # Print the loaded datetime object
    print("Loaded datetime:", loaded_dt)
    
    # Clean up the pickle file after demonstration
    if os.path.exists(FILE_NAME):
        os.remove(FILE_NAME)