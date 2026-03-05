
import pandas as pd
from statistics import mean
def task_func(df: pd.DataFrame) -> dict:
    if not df.columns.str.contains('Name|Score'):
        raise ValueError("DataFrame must have 'Name' and 'Score' columns")
    gen_dict = {}
    for name, score in df[['Name', 'Score']].itertuples(index=False):
        gen_dict[name] = (name, mean(score))
    return gen_dict