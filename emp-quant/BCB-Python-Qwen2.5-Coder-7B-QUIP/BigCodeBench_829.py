
import pandas as pd
from statistics import mean

def task_func(df: pd.DataFrame) -> dict:
    if 'Name' not in df or 'Score' not in df:
        raise ValueError("DataFrame must contain 'Name' and 'Score' columns")
    
    name_group = df.groupby('Name')['Score'].mean()
    gen_dict = {name: (name, score) for name, score in name_group.items()}
    
    return gen_dict

gen_dict = task_func(df_sample)
print({key: next(value) for key, value in gen_dict.items()})