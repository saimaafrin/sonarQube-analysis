
import numpy as np
from sklearn.preprocessing import OneHotEncoder

def task_func(list_of_lists):
    # Merge the list of lists into a single list
    merged_list = [item for sublist in list_of_lists for item in sublist]
    
    # Initialize the OneHotEncoder
    encoder = OneHotEncoder(sparse=False)
    
    # Fit and transform the merged list
    one_hot = encoder.fit_transform(merged_list)
    
    # Return the one-hot encoding as a numpy array
    return one_hot