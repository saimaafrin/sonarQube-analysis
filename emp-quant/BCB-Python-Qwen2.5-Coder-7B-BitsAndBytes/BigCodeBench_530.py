
import pandas as pd
import numpy as np
from collections import Counter
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df: pd.DataFrame) -> (Counter, plt.Axes):
    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("DataFrame is empty")
    
    # Round down ages to the nearest integer and filter out negative ages
    df['age'] = df['age'].apply(lambda x: int(x) if isinstance(x, float) else x)
    df = df[df['age'] >= 0]
    
    # Identify duplicate names
    duplicates = df[df.duplicated('name', keep=False)]
    
    # Record the age distribution for duplicate names
    age_distribution = Counter(duplicates['age'])
    
    # Create a histogram plot if there are duplicates
    if len(age_distribution) > 0:
        min_age = min(age_distribution.keys())
        max_age = max(age_distribution.keys())
        bin_edges = np.arange(min_age - 0.5, max_age + 1.5, 1)
        
        plt.figure(figsize=(10, 6))
        sns.histplot(data=duplicates, x='age', bins=bin_edges, kde=False)
        plt.xlabel('Age')
        plt.ylabel('Count')
        plt.title('Age Distribution Among Duplicate Names')
        plt.show()
    else:
        plt = None
    
    return age_distribution, plt