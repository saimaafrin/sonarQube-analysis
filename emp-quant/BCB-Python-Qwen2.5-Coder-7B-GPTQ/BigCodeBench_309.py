import numpy as np
import random
from sklearn.preprocessing import MinMaxScaler
def task_func(list_of_lists, seed=42):
    scaler = MinMaxScaler()
    random.seed(seed)
    
    for i in range(len(list_of_lists)):
        if not list_of_lists[i]:  # Check if the inner list is empty
            list_of_lists[i] = [random.randint(0, 100) for _ in range(5)]
    
    # Convert the list of lists to a numpy array
    array_of_lists = np.array(list_of_lists)
    
    # Reshape the array to a 2D array for scaling
    reshaped_array = array_of_lists.reshape(-1, 1)
    
    # Scale the values
    scaled_array = scaler.fit_transform(reshaped_array)
    
    # Reshape back to the original list of lists structure
    scaled_list_of_lists = scaled_array.reshape(len(list_of_lists), -1).tolist()
    
    return scaled_list_of_lists