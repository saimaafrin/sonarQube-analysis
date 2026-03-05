
import pickle
import os

# Constants
FILE_NAME = 'save.pkl'

def task_func(dt):
    # Save the date time object "dt" in the pickle file "save.pkl"
    with open(FILE_NAME, 'wb') as f:
        pickle.dump(dt, f)

    # Read the saved datetime object from the pickle file
    with open(FILE_NAME, 'rb') as f:
        loaded_dt = pickle.load(f)

    # Output the loaded datetime object
    print(loaded_dt)

# Call the function with a datetime object
dt = datetime.datetime(2023, 3, 14, 14, 30)
task_func(dt)