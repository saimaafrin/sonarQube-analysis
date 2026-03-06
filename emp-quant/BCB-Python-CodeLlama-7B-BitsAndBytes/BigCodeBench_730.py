
import pickle
import os

# Constants
FILE_NAME = 'save.pkl'

def task_func(dt):
    # Save the datetime object to a pickle file
    with open(FILE_NAME, 'wb') as f:
        pickle.dump(dt, f)

    # Read the pickle file back and print the loaded datetime object
    with open(FILE_NAME, 'rb') as f:
        loaded_dt = pickle.load(f)
        print(f'loaded_dt: {loaded_dt}')

# Create a datetime object
dt = datetime.now()

# Call the task function with the datetime object
task_func(dt)