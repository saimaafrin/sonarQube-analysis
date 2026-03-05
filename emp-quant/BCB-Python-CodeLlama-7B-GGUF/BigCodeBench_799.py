
import pandas as pd
from random import seed, choices

def task_func(L, num_dataframes=5, random_seed=None):
    if L == []:
        return pd.DataFrame(), []
    else:
        if random_seed:
            seed(random_seed)
        column_names = choices('abcdefghijklmnopqrstuvwxyz', k=len(L[0]))
        data = []
        for i in range(num_dataframes):
            data.append(pd.DataFrame(L, columns=column_names))
        common_rows = data[0].merge(data[1], on=column_names, how='inner')
        for i in range(2, num_dataframes):
            common_rows = common_rows.merge(data[i], on=column_names, how='inner')
        return common_rows, data

L = [[1, '65', 76], [2, '5', 6]]
common_rows, df_list = task_func(L, num_dataframes=1, random_seed=1)
print(common_rows)
print(df_list)