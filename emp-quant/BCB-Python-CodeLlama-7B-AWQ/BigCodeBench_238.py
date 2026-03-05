import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
def task_func(df):
    # Standardize 'Age' and 'Score' columns
    scaler = StandardScaler()
    df[['Age (standardized)', 'Score (standardized)']] = scaler.fit_transform(df[['Age', 'Score']])

    # Remove duplicates based on 'Name'
    df = df.drop_duplicates('Name')

    # Plot scatter plot of standardized values
    fig, ax = plt.subplots()
    ax.scatter(df['Age (standardized)'], df['Score (standardized)'])
    ax.set_title('Scatter Plot of Standardized Age and Score')
    ax.set_xlabel('Age (standardized)')
    ax.set_ylabel('Score (standardized)')
    return df, ax
df = pd.DataFrame({'Name': ['Alice', 'Alice', 'Bob', 'Bob', 'Charlie', 'Charlie'],
                   'Age': [25, 25, 30, 30, 35, 35],
                   'Score': [85, 90, 95, 100, 80, 85]})