
import pandas as pd
import numpy as np

def task_func(data_list=[('a', 1, 2.1), ('b', 2, 3.2), ('c', 3, 4.3), ('d', 4, 5.4), ('e', 5, 6.5)]):
    if not data_list:
        return pd.DataFrame(columns=['Mean Value'])
    
    # Initialize a dictionary to store the sum and count of numeric values at each position
    sums = [0] * len(data_list[0])
    counts = [0] * len(data_list[0])
    
    # Iterate over each tuple in the list
    for tup in data_list:
        for i, value in enumerate(tup):
            if isinstance(value, (int, float)):
                sums[i] += value
                counts[i] += 1
    
    # Calculate the mean for each position
    means = [sums[i] / counts[i] if counts[i] > 0 else np.nan for i in range(len(sums))]
    
    # Create a DataFrame with the results
    result_df = pd.DataFrame(means, columns=['Mean Value'], index=[f'Position {i}' for i in range(len(means))])
    
    return result_df