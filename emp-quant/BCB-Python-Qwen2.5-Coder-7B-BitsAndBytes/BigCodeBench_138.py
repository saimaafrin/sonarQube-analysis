
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df, letters=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')):
    # Check if df is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame")
    
    # Check if 'Letters' column exists in the DataFrame
    if 'Letters' not in df.columns:
        raise ValueError("'Letters' column is missing from the DataFrame")
    
    # Filter out non-letter characters and convert to uppercase
    df['Letters'] = df['Letters'].str.upper().str[0]
    
    # Create a frequency series
    freq_series = df['Letters'].value_counts()
    
    # Plotting the bar chart
    fig, ax = plt.subplots()
    ax.bar(freq_series.index, freq_series.values)
    ax.set_xlabel('Letters')
    ax.set_ylabel('Frequency')
    ax.set_title('Letter Frequency')
    
    return ax