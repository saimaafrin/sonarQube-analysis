import pandas as pd
import numpy as np
from collections import Counter
import seaborn as sns
import matplotlib.pyplot as plt
def task_func(df: pd.DataFrame) -> (Counter, plt.Axes):
    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("DataFrame is empty")
    
    # Round down ages to the nearest integer and ensure they are non-negative
    df['age'] = df['age'].apply(lambda x: int(np.floor(x)) if x >= 0 else np.nan)
    df = df.dropna(subset=['age'])
    
    # Identify duplicate names
    duplicates = df[df.duplicated('name', keep=False)]
    
    # Check if there are any duplicates
    if duplicates.empty:
        return Counter(), None
    
    # Record the age distribution for duplicate names
    age_distribution = Counter(duplicates['age'])
    
    # Create a histogram plot for the age distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(duplicates['age'], bins=np.arange(min(age_distribution.keys()), max(age_distribution.keys()) + 1.5) - 0.5, kde=False)
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.title('Age Distribution among Duplicate Names')
    
    return age_distribution, plt.gca()