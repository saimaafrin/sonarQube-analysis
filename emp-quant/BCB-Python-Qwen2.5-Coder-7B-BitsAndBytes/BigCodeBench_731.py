
import pickle
import os
from sklearn.datasets import make_classification

# Constants
FILE_NAME = 'save.pkl'
DATA, TARGET = make_classification(n_samples=100, n_features=20, n_informative=2, n_redundant=10, n_classes=2, random_state=1)

def task_func(data, target):
    # Save the data and target to a pickle file
    with open(FILE_NAME, 'wb') as f:
        pickle.dump((data, target), f)
    
    # Read the data and target from the pickle file
    with open(FILE_NAME, 'rb') as f:
        loaded_data, loaded_target = pickle.load(f)
    
    return loaded_data, loaded_target