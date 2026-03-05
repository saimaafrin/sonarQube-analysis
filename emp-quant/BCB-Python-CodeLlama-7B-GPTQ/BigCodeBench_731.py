import pickle
import os
from sklearn.datasets import make_classification
FILE_NAME = 'save.pkl'
def task_func(data, target):
    # Save the data and target to a pickle file
    with open(FILE_NAME, 'wb') as f:
        pickle.dump((data, target), f)

    # Read the data and target from the pickle file
    with open(FILE_NAME, 'rb') as f:
        loaded_data, loaded_target = pickle.load(f)

    # Check that the loaded data and target are the same as the original data and target
    assert loaded_data.equals(data)
    assert loaded_target.equals(target)

    # Return the loaded data and target
    return loaded_data, loaded_target