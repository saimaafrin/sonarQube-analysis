import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
def task_func(df):
    # Standardize 'Age' and 'Score' columns
    scaler = StandardScaler()
    df_std = scaler.fit_transform(df[['Age', 'Score']])

    # Remove duplicate entries based on 'Name'
    df_std = df_std.drop_duplicates(subset='Name', keep='first')

    # Plot a scatter plot of standardized values
    fig, ax = plt.subplots()
    ax.scatter(df_std['Age (standardized)'], df_std['Score (standardized)'])
    ax.set_title('Scatter Plot of Standardized Age and Score')
    ax.set_xlabel('Age (standardized)')
    ax.set_ylabel('Score (standardized)')
    plt.show()

    return df_std, ax
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35, 20, 30, 35],
    'Score': [85, 70, 60, 90, 80, 70]
})