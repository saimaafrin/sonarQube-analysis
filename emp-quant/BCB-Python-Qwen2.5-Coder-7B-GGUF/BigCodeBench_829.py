
import pandas as pd
from statistics import mean

def task_func(df: pd.DataFrame) -> dict:
    if 'Name' not in df.columns or 'Score' not in df.columns:
        raise ValueError("DataFrame must contain 'Name' and 'Score' columns")
    
    name_scores = df.groupby('Name')['Score'].mean().reset_index()
    gen_dict = {name: (name, score) for name, score in zip(name_scores['Name'], name_scores['Score'])}
    
    return gen_dict