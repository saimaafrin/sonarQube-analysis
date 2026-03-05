import numpy as np
from sklearn.preprocessing import OneHotEncoder
def task_func(list_of_lists):
    """
    Merges a predefined set of lists into a list and one-hot-encodes the elements of the list.
    """
    # Merge the lists
    merged_list = []
    for sublist in list_of_lists:
        merged_list.extend(sublist)

    # One-hot encode the merged list
    encoder = OneHotEncoder(sparse=False)
    one_hot = encoder.fit_transform(merged_list)

    return one_hot
list_of_lists = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]