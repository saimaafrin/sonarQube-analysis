import pandas as pd
import numpy as np
import itertools
def task_func(data_list=[('a', 1, 2.1), ('b', 2, 3.2), ('c', 3, 4.3), ('d', 4, 5.4), ('e', 5, 6.5)]):
    # Initialize a list to store the means of each position
    means = []
    
    # Iterate over each position using itertools.zip_longest to handle tuples of different lengths
    for values in itertools.zip_longest(*data_list, fillvalue=None):
        # Filter out non-numeric values and calculate the mean of the remaining numeric values
        numeric_values = [v for v in values if isinstance(v, (int, float))]
        if numeric_values:
            mean = np.mean(numeric_values)
        else:
            mean = np.nan
        means.append(mean)
    
    # Create a DataFrame with the means and appropriate index
    df = pd.DataFrame(means, index=[f'Position {i}' for i in range(len(means))], columns=['Mean Value'])
    
    return df
data = [('a', '1', 2.1), ('b', 21, 'c'), (12, 3, 4.3), (['d'], 4, 5.4), ('e', 5, 6.5)]