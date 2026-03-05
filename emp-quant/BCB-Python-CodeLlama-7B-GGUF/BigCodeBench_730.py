
import pickle
import os

# Constants
FILE_NAME = 'save.pkl'

def task_func(dt):
    # Save the datetime object to a pickle file
    with open(FILE_NAME, 'wb') as f:
        pickle.dump(dt, f)

    # Read the datetime object back from the pickle file
    with open(FILE_NAME, 'rb') as f:
        loaded_dt = pickle.load(f)

    # Print the loaded datetime object
    print(f'loaded_dt: {loaded_dt}')

# Create a datetime object
dt = datetime.now()

# Call the task function with the datetime object
task_func(dt)