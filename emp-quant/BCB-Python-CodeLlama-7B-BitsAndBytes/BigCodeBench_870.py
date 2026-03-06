
import pandas as pd
import numpy as np
import itertools

def task_func(data_list=[]):
    # Create an empty DataFrame with a single column and the appropriate index
    df = pd.DataFrame(index=range(len(data_list[0])), columns=['Mean Value'])

    # Iterate over the tuples in the list and calculate the mean of the numerical values
    for i, tup in enumerate(data_list):
        # Extract the numerical values from the tuple
        num_vals = [v for v in tup if isinstance(v, (int, float))]
        # Calculate the mean of the numerical values
        mean_val = np.mean(num_vals) if num_vals else np.nan
        # Add the mean value to the DataFrame
        df.loc[i, 'Mean Value'] = mean_val

    return df