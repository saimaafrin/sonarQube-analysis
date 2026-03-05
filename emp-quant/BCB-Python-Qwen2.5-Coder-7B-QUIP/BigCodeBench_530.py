
import pandas as pd
import numpy as np
from collections import Counter
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df: pd.DataFrame) -> (Counter, plt.Axes):
    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("DataFrame is empty")
    
    # Round down ages to the nearest integer
    df['age'] = df['age'].apply(lambda x: np.floor(x))
    
    # Check for negative ages
    if df['age'].min() < 0:
        raise ValueError("Age cannot be negative")
    
    # Identify duplicate names
    duplicate_names = df[df['name'].duplicated(keep=False)]['name']
    
    # Filter the DataFrame to only include duplicates
    df_duplicates = df[df['name'].isin(duplicate_names)]
    
    # Calculate the age distribution for duplicates
    age_distribution = df_duplicates['age'].value_counts().sort_index()
    
    # Create a histogram plot for the age distribution
    plt.figure(figsize=(8, 6))
    sns.histplot(df_duplicates['age'], bins=np.arange(age_distribution.index.min() - 0.5, age_distribution.index.max() + 1.5, 1))
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.title('Age Distribution Among Duplicate Names')
    
    # Return the Counter object and the histogram plot
    return Counter(age_distribution), plt.gca()