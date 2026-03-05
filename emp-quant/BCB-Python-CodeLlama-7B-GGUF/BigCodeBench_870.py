
import pandas as pd
import numpy as np
import itertools

def task_func(data_list=[]):
    # Create a DataFrame with one column for each position
    df = pd.DataFrame(index=range(len(data_list[0])), columns=['Mean Value'])

    # Iterate over each tuple in the list
    for i, t in enumerate(data_list):
        # Extract the numerical values from the tuple
        num_values = [v for v in t if isinstance(v, (int, float))]

        # Compute the mean of the numerical values
        mean_value = np.mean(num_values) if num_values else np.nan

        # Add the mean value to the DataFrame
        df.loc[i, 'Mean Value'] = mean_value

    return df