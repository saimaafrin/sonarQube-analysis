import pandas as pd
from statistics import mean
def task_func(df: pd.DataFrame) -> dict:
    # Check if the DataFrame contains the required columns
    if 'Name' not in df.columns or 'Score' not in df.columns:
        raise ValueError("DataFrame must contain 'Name' and 'Score' columns")
    
    # Group the DataFrame by 'Name' and calculate the average score for each group
    grouped = df.groupby('Name')['Score'].mean().reset_index()
    
    # Create a dictionary of generator objects
    gen_dict = {name: (name, score) for name, score in zip(grouped['Name'], grouped['Score'])}
    
    return gen_dict
df_sample = pd.DataFrame({
    'Name': ['Micky', 'Donald', 'Girl'],
    'Score': [25.2, 9, -1]
})