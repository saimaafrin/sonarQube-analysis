
import numpy as np
import random
from sklearn.preprocessing import MinMaxScaler

def task_func(list_of_lists, seed=42):
    # Initialize the scaler
    scaler = MinMaxScaler()

    # Fill the empty inner lists with random integers
    for i, inner_list in enumerate(list_of_lists):
        if not inner_list:
            list_of_lists[i] = [random.randint(0, 100) for _ in range(5)]

    # Scale the values
    scaled_values = scaler.fit_transform(list_of_lists)

    # Return the scaled values
    return scaled_values