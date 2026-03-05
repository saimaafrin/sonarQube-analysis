
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler

def task_func(df1, df2):
    # Merge the dataframes on 'id' column using outer join
    merged_df = pd.merge(df1, df2, on='id', how='outer')
    
    # Initialize the StandardScaler
    scaler = StandardScaler()
    
    # Fit and transform the numeric features from df1
    scaled_features = scaler.fit_transform(merged_df[['feature1', 'feature2']])
    
    # Replace the original numeric features in the merged dataframe with scaled features
    merged_df[['feature1', 'feature2']] = scaled_features
    
    # Create a pair plot of the scaled features from df1
    pair_plot = sns.pairplot(merged_df[['feature1', 'feature2']])
    
    return merged_df, pair_plot