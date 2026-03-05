from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
def task_func(df):
    # Standardize numeric columns
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df)

    # Replace missing values with column means
    df_scaled = df_scaled.fillna(df_scaled.mean())

    # Create correlation matrix
    corr = df_scaled.corr()

    # Plot heatmap
    sns.heatmap(corr, annot=True, cmap='coolwarm')

    # Return DataFrame and heatmap
    return df_scaled, corr
df = pd.DataFrame({'A': [1, 2, 3, 4, 5],
                   'B': [2, 4, 6, 8, 10],
                   'C': [3, 6, 9, 12, 15],
                   'D': [4, 8, 12, 16, 20]})