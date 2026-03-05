import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
def task_func(df):
    # Standardize 'Age' and 'Score' columns
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df[['Age', 'Score']])

    # Remove duplicates based on 'Name'
    df_scaled = df_scaled.drop_duplicates(subset='Name')

    # Plot scatter plot of standardized values
    fig, ax = plt.subplots()
    ax.scatter(df_scaled['Age (standardized)'], df_scaled['Score (standardized)'])
    ax.set_title('Scatter Plot of Standardized Age and Score')
    ax.set_xlabel('Age (standardized)')
    ax.set_ylabel('Score (standardized)')
    return df_scaled, ax
df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie'],
                   'Age': [25, 30, 35, 25, 30, 35],
                   'Score': [85, 90, 95, 85, 90, 95]})