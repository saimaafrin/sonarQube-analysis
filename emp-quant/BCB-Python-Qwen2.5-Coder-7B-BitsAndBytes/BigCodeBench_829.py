
import pandas as pd
from statistics import mean

def task_func(df: pd.DataFrame) -> dict:
    if 'Name' not in df.columns or 'Score' not in df.columns:
        raise ValueError("DataFrame must contain 'Name' and 'Score' columns")
    
    name_scores = df.groupby('Name')['Score'].mean().reset_index()
    gen_dict = {}
    
    for index, row in name_scores.iterrows():
        name = row['Name']
        avg_score = row['Score']
        
        def generate_tuple(name, avg_score):
            yield (name, avg_score)
        
        gen_dict[name] = generate_tuple(name, avg_score)
    
    return gen_dict