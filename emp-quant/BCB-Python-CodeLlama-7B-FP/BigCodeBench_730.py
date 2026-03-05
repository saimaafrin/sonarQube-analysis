import pickle
import os
FILE_NAME = 'save.pkl'
def task_func(dt):
    # Save the datetime object "dt" in the pickle file "save.pkl"
    with open(FILE_NAME, 'wb') as f:
        pickle.dump(dt, f)

    # Read the datetime object from the pickle file "save.pkl"
    with open(FILE_NAME, 'rb') as f:
        loaded_dt = pickle.load(f)

    # Validate the loaded datetime object
    assert loaded_dt == dt

    return loaded_dt
dt = datetime.now()