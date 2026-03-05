import pickle
import os
from sklearn.datasets import make_classification
FILE_NAME = 'save.pkl'
def task_func(data, target):
    # Save the data and target to a pickle file
    with open(FILE_NAME, 'wb') as file:
        pickle.dump((data, target), file)
    
    # Read the data and target from the pickle file
    with open(FILE_NAME, 'rb') as file:
        loaded_data, loaded_target = pickle.load(file)
    
    # Return the loaded data and target
    return loaded_data, loaded_target