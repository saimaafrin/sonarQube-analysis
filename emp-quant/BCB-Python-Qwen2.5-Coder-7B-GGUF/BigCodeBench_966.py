
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df: pd.DataFrame) -> pd.DataFrame:
    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("The DataFrame is empty.")
    
    # Check if the DataFrame contains non-numeric data
    if not all(df.dtypes.apply(lambda x: pd.api.types.is_numeric_dtype(x))):
        raise ValueError("The DataFrame contains non-numeric data.")
    
    # Calculate the cumulative sum for each column, treating NaN as zero
    cumulative_sum_df = df.fillna(0).cumsum()
    
    # Plot the cumulative sums in a bar chart
    cumulative_sum_df.plot(kind='bar', figsize=(10, 6))
    plt.title('Cumulative Sum per Column')
    plt.xlabel('Index')
    plt.ylabel('Cumulative Sum')
    plt.legend(title='Columns')
    plt.show()
    
    return cumulative_sum_df