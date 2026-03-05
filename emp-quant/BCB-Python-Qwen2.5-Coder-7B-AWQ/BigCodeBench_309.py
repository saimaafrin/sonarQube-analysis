import numpy as np
import random
from sklearn.preprocessing import MinMaxScaler
def task_func(list_of_lists, seed=42):
    """
    Scales the values in a list of lists to a (0,1) range using MinMaxScaler.
    If any inner list is empty, it fills it with five random integers between 0 and 100,
    and then scales the values.
    
    Parameters:
    - list_of_lists: List[List[int]], a list of lists containing integers.
    - seed: int, a seed for the random number generator to ensure reproducibility.
    
    Returns:
    - List[List[float]], a list of lists containing scaled values between the range [0, 1].
    """
    scaler = MinMaxScaler()
    result = []
    
    for sublist in list_of_lists:
        if not sublist:  # Check if the sublist is empty
            random.seed(seed)
            sublist = [random.randint(0, 100) for _ in range(5)]
        
        # Reshape the sublist to a 2D array for scaling
        sublist_reshaped = np.array(sublist).reshape(-1, 1)
        scaled_sublist = scaler.fit_transform(sublist_reshaped)
        
        # Convert the scaled values back to a list and append to the result
        result.append(scaled_sublist.flatten().tolist())
    
    return result
list_of_lists = [[1, 2, 3], [], [4, 5]]