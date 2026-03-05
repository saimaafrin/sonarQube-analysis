import numpy as np
import random
from sklearn.preprocessing import MinMaxScaler
def task_func(list_of_lists, seed=42):
    """
    Scale the values in a list of lists to a (0,1) range using MinMaxScaler.
    If any inner list is empty, the function fills it with five random integers between 0 and 100, and then scales the values.
    """
    # Initialize the scaler
    scaler = MinMaxScaler()

    # Fill empty inner lists with random integers between 0 and 100
    for i, inner_list in enumerate(list_of_lists):
        if not inner_list:
            list_of_lists[i] = [random.randint(0, 100) for _ in range(5)]

    # Scale the values
    scaled_list_of_lists = scaler.fit_transform(list_of_lists)

    return scaled_list_of_lists
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]