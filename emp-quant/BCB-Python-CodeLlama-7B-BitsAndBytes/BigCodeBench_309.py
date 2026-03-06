
import numpy as np
import random
from sklearn.preprocessing import MinMaxScaler

def task_func(list_of_lists, seed=42):
    # Initialize the scaler with the given seed
    scaler = MinMaxScaler(random_state=seed)

    # Fill any empty inner lists with random integers between 0 and 100
    for inner_list in list_of_lists:
        if not inner_list:
            inner_list.extend(random.sample(range(100), 5))

    # Scale the values in each inner list to the range [0, 1]
    scaled_list_of_lists = scaler.fit_transform(list_of_lists)

    return scaled_list_of_lists