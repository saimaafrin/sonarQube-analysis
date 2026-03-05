import pandas as pd
from random import seed, choices
def task_func(L, num_dataframes=5, random_seed=None):
    """
    Generate a specified number of Pandas DataFrames from a list of lists "L".
    Each DataFrame has the same column names randomly chosen from lowercase English letters and 3 rows sampled from 'L'.
    Then, find the common rows between all generated DataFrames.
    If L is empty, an empty dataframe is returned.
    """
    if L == []:
        return pd.DataFrame(), []

    # Set random seed for reproducibility
    if random_seed is not None:
        seed(random_seed)

    # Generate column names randomly
    column_names = choices(string.ascii_lowercase, k=3)

    # Generate DataFrames
    df_list = []
    for i in range(num_dataframes):
        df = pd.DataFrame(L, columns=column_names)
        df_list.append(df)

    # Find common rows
    common_rows = df_list[0].merge(df_list[1], on=column_names, how='inner')
    for i in range(2, len(df_list)):
        common_rows = common_rows.merge(df_list[i], on=column_names, how='inner')

    return common_rows, df_list
L = [[1, '65', 76], [2, '5', 6]]