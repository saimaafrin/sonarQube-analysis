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
    
    # Calculate Z-scores
    z_scores = value_columns.apply(zscore)
    
    # Replace 'Value' column with Z-scores
    df = df.drop(columns=['Value']).join(z_scores)
    
    # Create a box plot of Z-scores over time
    plt.figure(figsize=(10, 6))
    z_scores.boxplot()
    plt.title('Z-Scores Over Time')
    plt.xlabel('Date')
    plt.ylabel('Z-Score')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    return df