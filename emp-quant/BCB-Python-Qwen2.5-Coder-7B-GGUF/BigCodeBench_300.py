
import pandas as pd
from scipy.stats import zscore
import matplotlib.pyplot as plt

def task_func(df):
    # Check if 'Date' and 'Value' columns exist
    if 'Date' not in df.columns or 'Value' not in df.columns:
        raise KeyError("DataFrame must contain 'Date' and 'Value' columns")
    
    # Convert 'Date' to datetime
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Split 'Value' lists into separate columns
    value_columns = pd.DataFrame(df['Value'].tolist(), index=df.index)
    df = pd.concat([df, value_columns], axis=1)
    
    # Calculate Z-scores
    z_scores = df.drop(columns=['Date']).apply(zscore)
    df = pd.concat([df['Date'], z_scores], axis=1)
    
    # Create a box plot of Z-scores over time
    plt.figure(figsize=(10, 6))
    plt.boxplot(z_scores, vert=False)
    plt.title('Z-Scores Over Time')
    plt.xlabel('Date')
    plt.ylabel('Z-Score')
    plt.show()
    
    return df