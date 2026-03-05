
import numpy as np
from sklearn.preprocessing import OneHotEncoder

def task_func(list_of_lists):
    # Merge the lists
    merged_list = []
    for sublist in list_of_lists:
        merged_list.extend(sublist)

    # One-hot encode the merged list
    encoder = OneHotEncoder()
    one_hot = encoder.fit_transform(merged_list)

    return one_hot