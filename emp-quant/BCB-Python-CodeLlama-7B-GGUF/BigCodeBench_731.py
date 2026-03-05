
import pickle
import os
from sklearn.datasets import make_classification

# Constants
FILE_NAME = 'save.pkl'
DATA, TARGET = make_classification(n_samples=100, n_features=20, n_informative=2, n_redundant=10, n_classes=2, random_state=1)

def task_func(data, target):
    # Save the data to a pickle file
    with open(FILE_NAME, 'wb') as f:
        pickle.dump((data, target), f)

    # Read the data back from the pickle file
    with open(FILE_NAME, 'rb') as f:
        loaded_data = pickle.load(f)

    # Return the loaded data
    return loaded_data

# Call the task function
loaded_data = task_func(DATA, TARGET)

# Print the loaded data
print(loaded_data)