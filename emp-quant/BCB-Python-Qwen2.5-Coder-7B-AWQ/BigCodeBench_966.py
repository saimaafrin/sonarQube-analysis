import pandas as pd
import matplotlib.pyplot as plt
def task_func(df: pd.DataFrame) -> pd.DataFrame:
    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("The DataFrame is empty.")
    
    # Check if the DataFrame contains non-numeric data
    if not pd.api.types.is_numeric_dtype(df.dtypes):
        raise ValueError("The DataFrame contains non-numeric data.")
    
    # Calculate the cumulative sum for each column, treating NaN as zero
    cumulative_sums = df.fillna(0).cumsum()
    
    # Plot the cumulative sums in a bar chart
    cumulative_sums.plot(kind='bar', legend=True)
    plt.title('Cumulative Sum per Column')
    plt.xlabel('Index')
    plt.ylabel('Cumulative Sum')
    plt.show()
    
    return cumulative_sums
df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12]
})