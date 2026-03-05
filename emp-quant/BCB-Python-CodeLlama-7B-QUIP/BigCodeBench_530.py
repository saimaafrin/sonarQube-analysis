
import pandas as pd
import numpy as np
from collections import Counter
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df: pd.DataFrame) -> (Counter, plt.Axes):
    if df.empty:
        raise ValueError("DataFrame is empty")
    if any(df['age'] < 0):
        raise ValueError("Age is negative")
    # Identify duplicate names
    duplicates = df.groupby('name')['age'].count()
    # Calculate age distribution
    ages = df.groupby('name')['age'].mean()
    # Create Counter object
    counter = Counter(ages)
    # Create histogram plot
    fig, ax = plt.subplots()
    ax.hist(counter.keys(), bins=np.arange(0, 101, 1))
    ax.set_xlabel("Age")
    ax.set_ylabel("Count")
    ax.set_title("Age distribution among duplicate names")
    return counter, ax