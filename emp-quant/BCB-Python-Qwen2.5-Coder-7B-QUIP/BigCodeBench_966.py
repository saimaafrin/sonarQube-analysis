
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df: pd.DataFrame) -> pd.DataFrame:
    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("DataFrame is empty")
    
    # Check if the DataFrame contains only numeric data
    if not df.select_dtypes(include=['number']).empty:
        raise ValueError("DataFrame contains non-numeric data")
    
    # Calculate the cumulative sum for each column, ignoring NaN values
    cumulative_sums = df.fillna(0).cumsum()
    
    # Plot the cumulative sums in a bar chart
    fig, ax = plt.subplots()
    ax.bar(cumulative_sums.index, cumulative_sums.values, align='center', width=0.8)
    ax.set_title('Cumulative Sum per Column')
    ax.set_xlabel('Index')
    ax.set_ylabel('Cumulative Sum')
    ax.legend(df.columns)
    
    return cumulative_sums, fig