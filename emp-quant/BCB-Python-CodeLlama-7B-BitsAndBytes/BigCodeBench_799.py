
import pandas as pd
from random import seed, choices

def task_func(L, num_dataframes=5, random_seed=None):
    # Set the random seed if provided
    if random_seed is not None:
        seed(random_seed)

    # Create a list of column names
    column_names = ['a', 'b', 'c']

    # Create a list to store the generated DataFrames
    df_list = []

    # Generate the specified number of DataFrames
    for i in range(num_dataframes):
        # Create a new DataFrame with 3 rows and the same column names
        df = pd.DataFrame(data=L, columns=column_names, index=range(3))

        # Add the DataFrame to the list
        df_list.append(df)

    # Find the common rows between all generated DataFrames
    common_rows = df_list[0].merge(df_list[1], on=column_names, how='inner')

    # Return the common rows and the list of DataFrames
    return common_rows, df_list