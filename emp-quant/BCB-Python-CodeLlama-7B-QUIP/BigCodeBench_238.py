
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

def task_func(df):
    # Standardize the 'Age' and 'Score' columns
    scaler = StandardScaler()
    df[['Age', 'Score']] = scaler.fit_transform(df[['Age', 'Score']])

    # Remove duplicates based on 'Name'
    df = df.drop_duplicates(subset=['Name'])

    # Plot the scatter plot
    fig, ax = plt.subplots()
    ax.scatter(df['Age (standardized)'], df['Score (standardized)'])
    ax.set_xlabel('Age (standardized)')
    ax.set_ylabel('Score (standardized)')
    ax.set_title('Scatter Plot of Standardized Age and Score')
    return df, ax