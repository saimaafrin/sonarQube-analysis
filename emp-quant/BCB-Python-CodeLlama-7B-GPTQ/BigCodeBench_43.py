import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
def task_func(df):
    # Replace NaN values with the average of the column
    df = df.fillna(df.mean())

    # Calculate statistics for each numeric column
    stats = df.describe()

    # Create a list of matplotlib Axes objects for each numeric column
    axes = []
    for col in df.select_dtypes(include=np.number).columns:
        sns.distplot(df[col], bins=10, ax=axes.append(plt.subplot()))

    return (stats, axes)
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'B': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'C': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'D': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'E': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'F': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'G': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'H': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'I': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'J': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'K': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'L': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'M': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'N': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'O': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'P': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Q': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'R': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'S': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'T': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'U': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'V': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'W': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'X': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Y': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Z': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
})
stats = df.describe()
axes = []