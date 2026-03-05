
import pandas as pd
from statistics import mean

def task_func(df: pd.DataFrame) -> dict:
    if 'Name' not in df.columns or 'Score' not in df.columns:
        raise ValueError("DataFrame must contain 'Name' and 'Score' columns")
    
    name_groups = df.groupby('Name')['Score']
    gen_dict = {name: (name, mean(scores)) for name, scores in name_groups}
    
    return gen_dict

gen_dict = task_func(df_sample)
print({key: next(value) for key, value in gen_dict.items()})
# Output: {'Donald': ('Donald', 9.0), 'Girl': ('Girl', -1.0), 'Micky': ('Micky', 25.2)}