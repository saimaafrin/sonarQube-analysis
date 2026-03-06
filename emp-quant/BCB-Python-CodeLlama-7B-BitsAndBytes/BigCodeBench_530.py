
import pandas as pd
import numpy as np
from collections import Counter
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df: pd.DataFrame) -> (Counter, plt.Axes):
    # Check if the DataFrame is empty or if age is negative
    if df.empty or df['age'].min() < 0:
        raise ValueError("DataFrame is empty or age is negative")

    # Round down age to nearest integer if it is a float
    df['age'] = df['age'].astype(int)

    # Identify duplicate names and calculate age distribution
    duplicates = df[df.duplicated(subset=['name'], keep=False)]
    ages = duplicates['age'].value_counts()

    # Create a Counter object with the age distribution
    counter = Counter(ages)

    # Create a histogram plot with the age distribution
    fig, ax = plt.subplots()
    sns.histplot(x=ages, ax=ax, bins=np.arange(df['age'].min(), df['age'].max() + 1, 1))
    ax.set_xlabel('Age')
    ax.set_ylabel('Count')
    ax.set_title('Age Distribution among Duplicate Names')

    return counter, ax