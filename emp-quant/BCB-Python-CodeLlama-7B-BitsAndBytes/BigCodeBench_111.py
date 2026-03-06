
import pandas as pd
import seaborn as sns

def task_func(df):
    # Check if 'df' is a DataFrame and has the required columns
    if not isinstance(df, pd.DataFrame) or 'Date' not in df.columns or 'Time' not in df.columns or 'Temperature' not in df.columns:
        raise ValueError("'df' is not a DataFrame or lacks 'Date', 'Time', or 'Temperature' columns")

    # Create a new DataFrame with the required columns
    df_heatmap = df[['Date', 'Time', 'Temperature']]

    # Create a Seaborn heatmap with the DataFrame
    ax = sns.heatmap(df_heatmap, annot=True, cmap='coolwarm')

    # Return the heatmap
    return ax