
import pickle
import os
# Constants
FILE_NAME = 'save.pkl'
def task_func(dt):
    # Save the datetime object to a pickle file
    with open(FILE_NAME, 'wb') as file:
        pickle.dump(dt, file)
    
    # Read the datetime object back from the pickle file
    with open(FILE_NAME, 'rb') as file:
        loaded_dt = pickle.load(file)
    
    # Output the loaded datetime object
    print(f"loaded_dt (datetime): {loaded_dt}")
    
    # Clean up the pickle file
    os.remove(FILE_NAME)
    
    return loaded_dt