
import numpy as np
from sklearn.preprocessing import OneHotEncoder

def task_func(list_of_lists):
    # Merge the list of lists into a single list
    merged_list = [item for sublist in list_of_lists for item in sublist]
    
    # Initialize the OneHotEncoder
    encoder = OneHotEncoder(sparse=False)
    
    # Fit and transform the merged list to get the one-hot encoded array
    one_hot = encoder.fit_transform([[x] for x in merged_list])
    
    return one_hot