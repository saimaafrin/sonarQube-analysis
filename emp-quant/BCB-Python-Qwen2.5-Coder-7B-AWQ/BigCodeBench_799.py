import pandas as pd
from random import seed, choices
def task_func(L, num_dataframes=5, random_seed=None):
    if not L:
        return pd.DataFrame(), []
    
    if random_seed is not None:
        seed(random_seed)
    
    column_names = [chr(i) for i in range(97, 123)]  # Lowercase English letters
    df_list = []
    
    for _ in range(num_dataframes):
        selected_columns = choices(column_names, k=3)
        selected_data = choices(L, k=3)
        df = pd.DataFrame(selected_data, columns=selected_columns)
        df_list.append(df)
    
    common_rows = df_list[0]
    for df in df_list[1:]:
        common_rows = common_rows.merge(df, how='inner')
    
    return common_rows, df_list
L = [[1, '65', 76], [2, '5', 6]]