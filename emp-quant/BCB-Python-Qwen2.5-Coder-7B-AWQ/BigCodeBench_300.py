import pandas as pd
from scipy.stats import zscore
import matplotlib.pyplot as plt
def task_func(df):
    # Check if 'Date' and 'Value' columns exist in the DataFrame
    if 'Date' not in df.columns or 'Value' not in df.columns:
        raise KeyError("DataFrame must contain 'Date' and 'Value' columns")
    
    # Convert 'Date' column to datetime
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Split 'Value' lists into separate columns and calculate Z-scores
    z_scores = df['Value'].apply(zscore)
    z_scores = pd.DataFrame(z_scores.tolist(), index=df.index)
    df = pd.concat([df.drop('Value', axis=1), z_scores], axis=1)
    
    # Create a box plot of Z-scores over time
    plt.figure(figsize=(10, 6))
    plt.boxplot(z_scores.T)
    plt.title('Z-Scores Over Time')
    plt.xlabel('Date')
    plt.ylabel('Z-Score')
    plt.xticks(rotation=45)
    plt.show()
    
    return df