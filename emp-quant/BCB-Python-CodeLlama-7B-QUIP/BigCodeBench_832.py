
import pickle
import os

def task_func(filename, data):
    try:
        if not os.path.exists(os.path.dirname(filename)):
            os.makedirs(os.path.dirname(filename))
        with open(filename, 'wb') as f:
            pickle.dump(data, f)
        return True
    except:
        return False