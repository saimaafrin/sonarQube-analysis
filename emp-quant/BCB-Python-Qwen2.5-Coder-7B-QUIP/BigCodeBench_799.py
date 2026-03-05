
import pandas as pd
from random import seed, choices

def task_func(L, num_dataframes=5, random_seed=None):
    if not L:
        return pd.DataFrame(), []

    if random_seed is not None:
        seed(random_seed)

    column_names = 'abcdefghijklmnopqrstuvwxyz'
    df_list = []

    for _ in range(num_dataframes):
        columns = choices(column_names, k=3)
        sample = choices(L, k=3)
        df = pd.DataFrame(sample, columns=columns)
        df_list.append(df)

    common_rows = df_list[0].copy()
    for df in df_list[1:]:
        common_rows = common_rows[common_rows.isin(df).all(axis=1)]

    return common_rows, df_list