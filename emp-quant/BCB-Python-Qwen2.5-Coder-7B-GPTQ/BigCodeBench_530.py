import pandas as pd
import numpy as np
from collections import Counter
import seaborn as sns
import matplotlib.pyplot as plt
def task_func(df: pd.DataFrame) -> (Counter, plt.Axes):
    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("DataFrame is empty")
    
    # Round down ages to the nearest integer and ensure non-negative ages
    df['age'] = df['age'].apply(lambda x: int(x) if x >= 0 else np.nan)
    df = df.dropna(subset=['age'])
    
    # Identify duplicate names
    duplicates = df[df.duplicated('name', keep=False)]
    
    # Check if there are any duplicates
    if duplicates.empty:
        return Counter(), None
    
    # Record the age distribution for duplicate names
    age_distribution = duplicates['age'].value_counts().sort_index()
    
    # Create a histogram plot
    plt.figure(figsize=(10, 6))
    sns.histplot(duplicates['age'], bins=np.arange(age_distribution.index.min() - 0.5, age_distribution.index.max() + 1.5, 1), kde=False)
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.title('Age Distribution among Duplicate Names')
    
    return age_distribution, plt.gca()