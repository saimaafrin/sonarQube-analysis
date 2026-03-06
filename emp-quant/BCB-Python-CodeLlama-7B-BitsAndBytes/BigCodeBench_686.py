
import numpy as np
from sklearn.preprocessing import OneHotEncoder

def task_func(list_of_lists):
    # Merge the predefined sets of lists
    merged_list = np.concatenate(list_of_lists)

    # One-hot encode the merged list
    encoder = OneHotEncoder()
    one_hot = encoder.fit_transform(merged_list)

    return one_hot

one_hot = task_func(list_of_lists)
print(one_hot)