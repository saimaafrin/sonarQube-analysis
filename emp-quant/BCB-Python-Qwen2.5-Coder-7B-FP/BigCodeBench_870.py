import pandas as pd
import numpy as np
import itertools
def task_func(data_list=[('a', 1, 2.1), ('b', 2, 3.2), ('c', 3, 4.3), ('d', 4, 5.4), ('e', 5, 6.5)]):
    # Initialize a list to store the means
    means = []
    
    # Determine the maximum length of tuples in the list
    max_length = max(len(tup) for tup in data_list)
    
    # Iterate over each position
    for i in range(max_length):
        # Extract the i-th element from each tuple, ignoring non-numeric values
        values = [item[i] for item in data_list if i < len(item) and isinstance(item[i], (int, float))]
        
        # Calculate the mean of the values at this position, or NaN if no values are present
        mean_value = np.mean(values) if values else np.nan
        
        # Append the mean value to the list
        means.append(mean_value)
    
    # Create a DataFrame with the means
    df = pd.DataFrame(means, columns=['Mean Value'], index=[f'Position {i}' for i in range(max_length)])
    
    return df
data = [('a', '1', 2.1), ('b', 21, 'c'), (12, 3, 4.3), (['d'], 4, 5.4), ('e', 5, 6.5)]