import pickle
import os
from sklearn.datasets import make_classification
FILE_NAME = 'save.pkl'
def task_func(data, target):
    # Save the data and target to a pickle file
    with open(FILE_NAME, 'wb') as file:
        pickle.dump((data, target), file)
    
    # Check if the file is saved successfully
    if not os.path.exists(FILE_NAME):
        raise FileNotFoundError("The file was not saved successfully.")
    
    # Read the data and target from the pickle file
    with open(FILE_NAME, 'rb') as file:
        loaded_data, loaded_target = pickle.load(file)
    
    # Check if the loaded data and target are the same as the original
    if not (np.array_equal(data, loaded_data) and np.array_equal(target, loaded_target)):
        raise ValueError("The loaded data and target are not the same as the original.")
    
    return loaded_data, loaded_target