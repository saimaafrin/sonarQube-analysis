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
        # Create the directory if it does not exist
        os.makedirs(directory)

    # Serialize the data using pickle
    with open(filename, 'wb') as f:
        pickle.dump(data, f)

    # Check if the file was written successfully
    if os.path.exists(filename):
        return True
    else:
        return False
filename = 'data.pkl'
data = {'key': 'value'}