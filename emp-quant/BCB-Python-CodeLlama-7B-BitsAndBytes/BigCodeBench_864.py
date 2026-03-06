
import pandas as pd
import numpy as np

def task_func(fruit_data):
    # Create an empty DataFrame with the appropriate columns and index
    df = pd.DataFrame(index=pd.Index([], name='Fruit'), columns=['Total Count', 'Average Count'])

    # Iterate over the fruit data and calculate the total and average counts for each fruit
    for fruit, count in fruit_data:
        # Check if the fruit is already in the DataFrame
        if fruit in df.index:
            # If it is, update the total count and average count for that fruit
            df.loc[fruit, 'Total Count'] += count
            df.loc[fruit, 'Average Count'] = df.loc[fruit, 'Total Count'] / df.loc[fruit, 'Count']
        else:
            # If it's not, add a new row for that fruit with the total and average count
            df = df.append(pd.Series([count, count / count], index=['Total Count', 'Average Count'], name=fruit))

    # Sort the DataFrame by the fruit index
    df.sort_index(inplace=True)

    return df