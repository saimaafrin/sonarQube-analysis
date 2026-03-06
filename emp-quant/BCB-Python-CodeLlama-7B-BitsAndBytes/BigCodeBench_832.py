
import pickle
import os

def task_func(filename, data):
    # Check if the directory exists
    dirname = os.path.dirname(filename)
    if not os.path.exists(dirname):
        os.makedirs(dirname)

    # Serialize the data and write it to the file
    with open(filename, 'wb') as f:
        pickle.dump(data, f)

    return True