import pickle
import os
def task_func(filename, data):
    """
    Serialize an object using pickle and overwrite the specified file with this serialized data.
    Before writing, checks if the directory exists, creating it if necessary.
    The function should output with:
        bool: True if the operation is successful, False otherwise.
    """
    # Check if the directory exists
    directory = os.path.dirname(filename)
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Write the data to the file
    with open(filename, 'wb') as f:
        pickle.dump(data, f)

    return True
data = {'a': 1, 'b': 2, 'c': 3}
filename = 'test.pkl'