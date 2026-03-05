import numpy as np
import random
from sklearn.preprocessing import MinMaxScaler
def task_func(list_of_lists, seed=42):
    """
    Scale the values in a list of lists to a (0,1) range using MinMaxScaler.
    If any inner list is empty, the function fills it with five random integers between 0 and 100, and then scales the values.
    """
    # Check if any inner list is empty
    if any(not inner_list for inner_list in list_of_lists):
        # Fill empty inner lists with random integers between 0 and 100
        for inner_list in list_of_lists:
            if not inner_list:
                inner_list.extend(random.sample(range(100), 5))

    # Create a MinMaxScaler object
    scaler = MinMaxScaler()

    # Scale the values in each inner list
    scaled_list_of_lists = []
    for inner_list in list_of_lists:
        scaled_inner_list = scaler.fit_transform(inner_list)
        scaled_list_of_lists.append(scaled_inner_list)

    return scaled_list_of_lists
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]