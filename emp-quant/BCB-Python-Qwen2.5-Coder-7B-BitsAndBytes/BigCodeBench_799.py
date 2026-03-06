
import pandas as pd
from random import seed, choices

def task_func(L, num_dataframes=5, random_seed=None):
    if not L:
        return pd.DataFrame(), []
    
    if random_seed is not None:
        seed(random_seed)
    
    columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    df_list = []
    
    for _ in range(num_dataframes):
        selected_columns = choices(columns, k=3)
        sample_df = pd.DataFrame(choices(L, k=3), columns=selected_columns)
        df_list.append(sample_df)
    
    common_rows = df_list[0].copy()
    for df in df_list[1:]:
        common_rows = common_rows.merge(df, how='inner')
    
    return common_rows, df_list