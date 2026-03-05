import pandas as pd
from random import seed, choices
def task_func(L, num_dataframes=5, random_seed=None):
    """
    Generate a specified number of Pandas DataFrames from a list of lists "L".
    Each DataFrame has the same column names randomly chosen from lowercase English letters and 3 rows sampled from 'L'.
    Then, find the common rows between all generated DataFrames.
    If L is empty, an empty dataframe is returned.
    """
    # Set random seed if provided
    if random_seed:
        seed(random_seed)

    # Create a list of column names
    column_names = list(choices(string.ascii_lowercase, k=3))

    # Create a list of DataFrames
    df_list = []
    for i in range(num_dataframes):
        # Create a DataFrame with the same column names and 3 rows sampled from L
        df = pd.DataFrame(data=L, columns=column_names)
        df = df.sample(n=3, random_state=i)
        df_list.append(df)

    # Find the common rows between all generated DataFrames
    common_rows = pd.concat(df_list, ignore_index=True).drop_duplicates()

    # Return the common rows and the list of DataFrames
    return common_rows, df_list
L = [[1, '65', 76], [2, '5', 6]]