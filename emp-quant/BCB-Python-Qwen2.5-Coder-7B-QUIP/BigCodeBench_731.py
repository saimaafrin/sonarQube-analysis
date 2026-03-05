
import pickle
import os
from sklearn.datasets import make_classification
# Constants
FILE_NAME = 'save.pkl'
DATA, TARGET = make_classification(n_samples=100, n_features=20, n_informative=2, n_redundant=10, n_classes=2, random_state=1)

def task_func(data, target):
    # Save the data and target to a pickle file
    with open(FILE_NAME, 'wb') as file:
        pickle.dump((data, target), file)
    
    # Read the data and target from the pickle file
    with open(FILE_NAME, 'rb') as file:
        loaded_data, loaded_target = pickle.load(file)
    
    # Validate the loaded data and target
    return (loaded_data, loaded_target)