import pandas as pd
import numpy as np
import itertools
def task_func(data_list=[('a', 1, 2.1), ('b', 2, 3.2), ('c', 3, 4.3), ('d', 4, 5.4), ('e', 5, 6.5)]):
    # Initialize a list to store the means
    means = []
    
    # Iterate over each position using itertools.zip_longest to handle tuples of different lengths
    for position in itertools.zip_longest(*data_list, fillvalue=None):
        # Filter out non-numeric values
        numeric_values = [value for value in position if isinstance(value, (int, float))]
        
        # Calculate the mean if there are numeric values, otherwise append NaN
        if numeric_values:
            mean_value = np.mean(numeric_values)
        else:
            mean_value = np.nan
        
        # Append the mean to the list
        means.append(mean_value)
    
    # Create a DataFrame with the means
    df = pd.DataFrame(means, columns=['Mean Value'], index=[f'Position {i}' for i in range(len(means))])
    
    return df
data = [('a', '1', 2.1), ('b', 21, 'c'), (12, 3, 4.3), (['d'], 4, 5.4), ('e', 5, 6.5)]