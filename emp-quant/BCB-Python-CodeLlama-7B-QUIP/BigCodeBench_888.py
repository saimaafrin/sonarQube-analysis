
import pandas as pd
import os

def task_func(data_dir: str, csv_files: list) -> pd.DataFrame:
    if not csv_files:
        return pd.DataFrame()
    dfs = []
    for file in csv_files:
        df = pd.read_csv(os.path.join(data_dir, file))
        dfs.append(df)
    return pd.concat(dfs)