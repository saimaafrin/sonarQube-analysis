import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler
def task_func(df1, df2):
    """
    Merges two dataframes on the 'id' column and scales the numeric features from df1.
    
    Parameters:
    - df1 (pd.DataFrame): The first dataframe with numeric features to be scaled.
    - df2 (pd.DataFrame): The second dataframe to be merged with df1.
    
    Returns:
    - merged_df (pd.DataFrame): The partially scaled and merged dataframe.
    - pair_plot (seaborn.axisgrid.PairGrid): Pair plot of the scaled dataframe.
    """
    # Merge the dataframes on 'id' column using outer join
    merged_df = pd.merge(df1, df2, on='id', how='outer')
    
    # Initialize the StandardScaler
    scaler = StandardScaler()
    
    # Fit and transform the numeric features from df1
    scaled_features = scaler.fit_transform(merged_df[['feature1', 'feature2']])
    
    # Replace the original numeric features in merged_df with the scaled features
    merged_df[['feature1', 'feature2']] = scaled_features
    
    # Create a pair plot of the scaled dataframe
    pair_plot = sns.pairplot(merged_df[['feature1', 'feature2']])
    
    return merged_df, pair_plot