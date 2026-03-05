
import pandas as pd
import numpy as np
import itertools

def task_func(data_list=[('a', 1, 2.1), ('b', 2, 3.2), ('c', 3, 4.3), ('d', 4, 5.4), ('e', 5, 6.5)]):
    if not data_list:
        return pd.DataFrame(columns=['Mean Value'])
    
    # Initialize a list to store the means for each position
    means = []
    
    # Iterate over each position
    for i in range(max(len(tup) for tup in data_list)):
        # Extract the value at the current position from each tuple
        values = [tup[i] for tup in data_list if i < len(tup)]
        
        # Filter out non-numeric values
        numeric_values = [val for val in values if isinstance(val, (int, float))]
        
        # Calculate the mean if there are numeric values, otherwise append NaN
        if numeric_values:
            mean_value = np.mean(numeric_values)
        else:
            mean_value = np.nan
        
        means.append(mean_value)
    
    # Create a DataFrame with the means
    df = pd.DataFrame(means, columns=['Mean Value'], index=[f'Position {i}' for i in range(len(means))])
    
    return df