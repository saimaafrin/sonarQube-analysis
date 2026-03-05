import pandas as pd
from random import seed, choices
def task_func(L, num_dataframes=5, random_seed=None):
    if random_seed is not None:
        seed(random_seed)
    
    if not L:
        return pd.DataFrame(), []
    
    column_names = [chr(i) for i in range(97, 123)]  # Generate lowercase English letters
    df_list = []
    
    for _ in range(num_dataframes):
        # Randomly choose 3 rows from L
        sampled_rows = choices(L, k=3)
        # Randomly choose column names
        selected_columns = choices(column_names, k=3)
        # Create DataFrame
        df = pd.DataFrame(sampled_rows, columns=selected_columns)
        df_list.append(df)
    
    # Find common rows between all DataFrames
    common_rows = df_list[0]
    for df in df_list[1:]:
        common_rows = common_rows.merge(df, on=list(common_rows.columns), how='inner')
    
    return common_rows, df_list
L = [[1, '65', 76], [2, '5', 6]]