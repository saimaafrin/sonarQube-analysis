
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df: pd.DataFrame) -> pd.DataFrame:
    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("DataFrame is empty")
    
    # Check if all columns contain numeric data
    if not all(pd.api.types.is_numeric_dtype(col) for col in df.dtypes):
        raise ValueError("DataFrame contains non-numeric data")
    
    # Calculate cumulative sum for each column, treating NaNs as 0
    cumsum_df = df.fillna(0).cumsum()
    
    # Plotting the cumulative sum
    fig, ax = plt.subplots()
    cumsum_df.plot(kind='bar', ax=ax)
    ax.set_title('Cumulative Sum per Column')
    ax.set_xlabel('Index')
    ax.set_ylabel('Cumulative Sum')
    ax.legend(title='Columns')
    
    return cumsum_df, fig