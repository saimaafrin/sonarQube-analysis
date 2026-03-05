import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
def task_func(df):
    """
    Normalize numeric columns in a DataFrame and draw a box plot for each column.
    Missing values are replaced by column's average.
    """
    # Normalize numeric columns
    scaler = MinMaxScaler()
    df_scaled = scaler.fit_transform(df)

    # Replace missing values with column average
    df_scaled = df_scaled.fillna(df_scaled.mean())

    # Draw box plots
    fig, ax = plt.subplots(figsize=(10, 6))
    for col in df_scaled.columns:
        ax.boxplot(df_scaled[col])
        ax.set_title(f"Box plot for {col}")
        ax.set_xlabel("Value")
        ax.set_ylabel("Frequency")
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_yticklabels([])
        ax.set_ylim(0, 1)
        ax.set_xlim(0, 1)
        ax.grid(True)

    return df_scaled, ax
df = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [10, 20, 30, 40, 50], "C": [100, 200, 300, 400, 500]})