
import pickle
import os

def task_func(filename, data):
    try:
        # Ensure the directory exists
        directory = os.path.dirname(filename)
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        # Serialize the data and write to the file
        with open(filename, 'wb') as file:
            pickle.dump(data, file)
        
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False