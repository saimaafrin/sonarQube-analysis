import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler
def task_func(df1, df2):
    """
    Merges two dataframes on the 'id' column and scales the numeric features from df1.
    
    Parameters:
    - df1 (pd.DataFrame): The first dataframe with numeric features to be scaled.
    - df2 (pd.DataFrame): The second dataframe to be merged with df1 on the 'id' column.
    
    Returns:
    - merged_df (pd.DataFrame): The partially scaled and merged dataframe.
    - pair_plot (seaborn.axisgrid.PairGrid): Pair plot of the scaled dataframe.
    """
    # Merge the dataframes on 'id' column using outer join
    merged_df = pd.merge(df1, df2, on='id', how='outer')
    
    # Select numeric columns from df1
    numeric_cols = df1.select_dtypes(include=[float, int]).columns
    
    # Initialize the StandardScaler
    scaler = StandardScaler()
    
    # Fit and transform the numeric columns from df1
    scaled_numeric_cols = scaler.fit_transform(df1[numeric_cols])
    
    # Replace the numeric columns in the merged dataframe with the scaled values
    for col, scaled_col in zip(numeric_cols, scaled_numeric_cols.T):
        merged_df[col] = scaled_col
    
    # Create a pair plot of the scaled dataframe
    pair_plot = sns.pairplot(merged_df[numeric_cols])
    
    return merged_df, pair_plot