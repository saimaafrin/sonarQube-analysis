
import pickle
import os

def task_func(filename, data):
    # Check if the directory exists, create it if necessary
    directory = os.path.dirname(filename)
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Serialize the data and write to the file
    try:
        with open(filename, 'wb') as file:
            pickle.dump(data, file)
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False