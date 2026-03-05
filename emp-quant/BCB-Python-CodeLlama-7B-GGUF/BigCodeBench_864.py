
import pandas as pd
import numpy as np

def task_func(fruit_data):
    # Create an empty DataFrame with the required columns
    df = pd.DataFrame(columns=['Total Count', 'Average Count'])

    # Iterate over the fruit data and calculate the total and average counts
    for fruit, count in fruit_data:
        # Check if the fruit is already in the DataFrame
        if fruit in df.index:
            # If the fruit is already in the DataFrame, add the count to the total count and update the average count
            df.loc[fruit, 'Total Count'] += count
            df.loc[fruit, 'Average Count'] = df.loc[fruit, 'Total Count'] / count
        else:
            # If the fruit is not in the DataFrame, add a new row with the count and average count
            df = df.append({'Total Count': count, 'Average Count': count}, ignore_index=True)

    # Sort the DataFrame by the fruit name
    df.sort_index(inplace=True)

    return df