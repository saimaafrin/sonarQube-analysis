import pandas as pd
import matplotlib.pyplot as plt
def task_func(df: pd.DataFrame) -> pd.DataFrame:
    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("The DataFrame is empty.")
    
    # Check if the DataFrame contains non-numeric data
    if not all(df.dtypes.apply(lambda x: np.issubdtype(x, np.number))):
        raise ValueError("The DataFrame contains non-numeric data.")
    
    # Calculate the cumulative sum for each column, treating NaN as zero
    cumsum_df = df.fillna(0).cumsum()
    
    # Plot the cumulative sums in a bar chart
    cumsum_df.plot(kind='bar', legend=True)
    plt.title('Cumulative Sum per Column')
    plt.xlabel('Index')
    plt.ylabel('Cumulative Sum')
    plt.show()
    
    return cumsum_df