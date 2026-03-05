
import pandas as pd
import numpy as np
import itertools

def task_func(data_list=[('a', 1, 2.1), ('b', 2, 3.2), ('c', 3, 4.3), ('d', 4, 5.4), ('e', 5, 6.5)]):
    if not data_list:
        return pd.DataFrame(columns=['Mean Value'])
    
    # Extract numerical values from each tuple
    numerical_values = []
    for item in data_list:
        numeric_values = [value for value in item if isinstance(value, (int, float))]
        numerical_values.append(numeric_values)
    
    # Calculate mean for each position
    means = []
    for position in range(max(len(values) for values in numerical_values)):
        column_values = [values[position] for values in numerical_values if position < len(values)]
        if column_values:
            means.append(np.mean(column_values))
        else:
            means.append(np.nan)
    
    # Create DataFrame
    df = pd.DataFrame(means, columns=['Mean Value'], index=[f'Position {i}' for i in range(len(means))])
    return df