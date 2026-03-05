
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler

def task_func(df1, df2):
    # Merge the dataframes on the 'id' column using outer join
    merged_df = pd.merge(df1, df2, on='id', how='outer')
    
    # Initialize the StandardScaler
    scaler = StandardScaler()
    
    # Fit and transform the numeric features from df1
    scaled_features = scaler.fit_transform(merged_df[merged_df.columns[merged_df.columns != 'id']])
    
    # Replace the original numeric features with the scaled ones
    merged_df[merged_df.columns[merged_df.columns != 'id']] = scaled_features
    
    # Create a pair plot of the scaled features
    pair_plot = sns.pairplot(merged_df[merged_df.columns[merged_df.columns != 'id']])
    
    # Return the partially scaled and merged dataframe and the pair plot
    return merged_df, pair_plot