
import pandas as pd
from random import seed, choices
def task_func(L, num_dataframes=5, random_seed=None):
    if len(L) == 0:
        return pd.DataFrame(), []
    if random_seed:
        seed(random_seed)
    df_list = []
    for i in range(num_dataframes):
        df = pd.DataFrame(L)
        df.columns = choices(df.columns, 3)
        df = df.sample(3)
        df_list.append(df)
    common_rows = df_list[0].merge(df_list[1], on=df_list[0].columns)
    return common_rows, df_list