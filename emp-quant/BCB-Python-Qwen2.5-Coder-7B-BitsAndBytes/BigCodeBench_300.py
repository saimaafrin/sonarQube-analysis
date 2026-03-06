
import pandas as pd
from scipy.stats import zscore
import matplotlib.pyplot as plt

def task_func(df):
    # Check if required columns exist
    if 'Date' not in df.columns or 'Value' not in df.columns:
        raise KeyError("DataFrame must contain 'Date' and 'Value' columns.")
    
    # Convert 'Date' to datetime
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Split 'Value' lists into separate columns
    value_columns = pd.DataFrame(df['Value'].tolist(), index=df.index)
    df = pd.concat([df.drop('Value', axis=1), value_columns], axis=1)
    
    # Calculate Z-scores
    z_scores = df.iloc[:, 1:].apply(zscore)
    df.iloc[:, 1:] = z_scores
    
    # Create a box plot for Z-scores over time
    fig, ax = plt.subplots()
    ax.boxplot(z_scores.T)
    ax.set_title('Z-Scores Over Time')
    ax.set_xlabel('Date')
    ax.set_ylabel('Z-Score')
    
    return df, fig