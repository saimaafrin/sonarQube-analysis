
import numpy as np
import random
from sklearn.preprocessing import MinMaxScaler

def task_func(list_of_lists, seed=42):
    # Initialize the scaler with the given seed
    scaler = MinMaxScaler(random_state=seed)

    # If any inner list is empty, fill it with random integers between 0 and 100
    for i, inner_list in enumerate(list_of_lists):
        if not inner_list:
            list_of_lists[i] = np.random.randint(0, 100, size=5)

    # Scale the values in each inner list using the scaler
    scaled_list_of_lists = []
    for inner_list in list_of_lists:
        scaled_inner_list = scaler.fit_transform(inner_list.reshape(-1, 1))
        scaled_list_of_lists.append(scaled_inner_list)

    return scaled_list_of_lists