import numpy as np
import random
from sklearn.preprocessing import MinMaxScaler
def task_func(list_of_lists, seed=42):
    """
    Scale the values in a list of lists to a (0,1) range using MinMaxScaler.
    If any inner list is empty, fill it with five random integers between 0 and 100,
    and then scale the values.
    
    Parameters:
    - list_of_lists: List[List[int]], a list of lists containing integers.
    - seed: int, seed for random number generation.
    
    Returns:
    - List[List[float]], a list of lists containing scaled values between the range [0, 1].
    """
    scaler = MinMaxScaler()
    result = []
    random.seed(seed)
    
    for sublist in list_of_lists:
        if not sublist:
            # Fill empty list with five random integers between 0 and 100
            sublist = [random.randint(0, 100) for _ in range(5)]
        # Reshape the sublist to a 2D array for scaling
        scaled_sublist = scaler.fit_transform(np.array(sublist).reshape(-1, 1))
        # Flatten the scaled sublist back to a list
        result.append(scaled_sublist.flatten().tolist())
    
    return result
list_of_lists = [[1, 2, 3], [], [4, 5]]