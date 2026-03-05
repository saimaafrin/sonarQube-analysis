
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
    ax.scatter(df['Age (standardized)'], df['Score (standardized)'], c='blue')
    ax.set_title('Scatter Plot of Standardized Age and Score')
    ax.set_xlabel('Age (standardized)')
    ax.set_ylabel('Score (standardized)')
    plt.show()
    
    return df, ax