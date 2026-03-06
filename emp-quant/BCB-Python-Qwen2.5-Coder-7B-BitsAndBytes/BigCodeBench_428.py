
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler

def task_func(df1, df2):
    # Merge the dataframes on 'id' using an outer join
    merged_df = pd.merge(df1, df2, on='id', how='outer')
    
    # Identify numeric columns in df1
    numeric_cols = df1.select_dtypes(include=[np.number]).columns
    
    # Scale the numeric features from df1
    scaler = StandardScaler()
    merged_df[numeric_cols] = scaler.fit_transform(merged_df[numeric_cols])
    
    # Create a pair plot of the scaled features from df1
    pair_plot = sns.pairplot(merged_df[numeric_cols], diag_kind='kde')
    
    return merged_df, pair_plot