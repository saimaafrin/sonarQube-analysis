
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler

def task_func(df1, df2):
    # Merge the dataframes on the 'id' column using an outer join
    merged_df = pd.merge(df1, df2, on='id', how='outer')
    
    # Select the numeric columns from df1
    numeric_columns = df1.select_dtypes(include=[int, float]).columns
    
    # Initialize the StandardScaler
    scaler = StandardScaler()
    
    # Fit and transform the numeric columns of df1
    scaled_numeric_columns = scaler.fit_transform(df1[numeric_columns])
    
    # Replace the numeric columns in the merged dataframe with the scaled values
    merged_df[numeric_columns] = scaled_numeric_columns
    
    # Create a pair plot of the scaled features from df1
    pair_plot = sns.pairplot(merged_df[numeric_columns])
    
    return merged_df, pair_plot