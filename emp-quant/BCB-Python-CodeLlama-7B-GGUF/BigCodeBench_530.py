
import pandas as pd
import numpy as np
from collections import Counter
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df: pd.DataFrame) -> (Counter, plt.Axes):
    # Check if the DataFrame is empty or if age is negative
    if df.empty or (df['age'] < 0).any():
        raise ValueError("DataFrame is empty or age is negative")

    # Round down age to the nearest integer if it is a float
    df['age'] = df['age'].astype(int)

    # Identify duplicate names and calculate age distribution
    duplicates = df[df.duplicated(subset=['name'], keep=False)]
    age_counts = Counter(duplicates['age'])

    # Calculate the minimum and maximum ages found among the duplicates
    min_age = min(age_counts.keys())
    max_age = max(age_counts.keys())

    # Calculate the bins for the histogram
    bins = np.arange(min_age - 0.5, max_age + 1, 1)

    # Create the histogram plot
    fig, ax = plt.subplots()
    sns.histplot(data=duplicates, x='age', y='count', bins=bins, ax=ax)
    ax.set_xlabel('Age')
    ax.set_ylabel('Count')
    ax.set_title('Age Distribution among Duplicate Names')

    return age_counts, ax