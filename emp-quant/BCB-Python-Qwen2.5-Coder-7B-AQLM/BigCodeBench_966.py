
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        raise ValueError("The DataFrame is empty.")
    
    if not all(df.dtypes.apply(lambda x: pd.api.types.is_numeric_dtype(x))):
        raise ValueError("The DataFrame contains non-numeric data.")
    
    # Replace NaN values with 0 for the purpose of cumulative sum calculation
    df_filled = df.fillna(0)
    
    # Calculate cumulative sum for each column
    cumulative_sum_df = df_filled.cumsum()
    
    # Plotting the cumulative sum
    cumulative_sum_df.plot(kind='bar', legend=True)
    plt.title('Cumulative Sum per Column')
    plt.xlabel('Index')
    plt.ylabel('Cumulative Sum')
    plt.show()
    
    return cumulative_sum_df