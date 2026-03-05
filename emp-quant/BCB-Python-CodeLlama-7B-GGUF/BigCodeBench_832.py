
import pickle
import os

def task_func(filename, data):
    # Check if the directory exists
    dirname = os.path.dirname(filename)
    if not os.path.exists(dirname):
        # Create the directory if it doesn't exist
        os.makedirs(dirname)

    # Open the file in binary mode
    with open(filename, 'wb') as f:
        # Serialize the data using pickle
        pickle.dump(data, f)

    # Return True if the operation is successful
    return True