
import pandas as pd
import numpy as np
from collections import Counter
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df: pd.DataFrame) -> (Counter, plt.Axes):
    if df.empty:
        raise ValueError("DataFrame is empty")
    
    # Round down ages to the nearest integer and ensure they are non-negative
    df['age'] = df['age'].apply(lambda x: np.floor(x) if x >= 0 else np.nan)
    if df['age'].isnull().any():
        raise ValueError("Age cannot be negative")
    
    # Identify duplicate names
    duplicates = df[df.duplicated('name', keep=False)]
    
    # Record the age distribution for duplicate names
    age_distribution = Counter(duplicates['age'])
    
    # Create a histogram plot if there are duplicates
    if not duplicates.empty:
        min_age = duplicates['age'].min()
        max_age = duplicates['age'].max()
        bins = np.arange(min_age, max_age + 1.5, 1)
        plt.figure(figsize=(10, 6))
        sns.histplot(duplicates['age'], bins=bins, kde=False)
        plt.xlabel('Age')
        plt.ylabel('Count')
        plt.title('Age Distribution among Duplicate Names')
        plt.show()
    else:
        plt = None
    
    return age_distribution, plt