
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler

def task_func(df1, df2):
    # Merge the two dataframes on the 'id' column
    merged_df = pd.merge(df1, df2, on='id', how='outer')

    # Scale the numeric features from df1
    scaler = StandardScaler()
    scaled_df = scaler.fit_transform(merged_df.select_dtypes(include=['number']))

    # Create a pair plot of the scaled features
    pair_plot = sns.pairplot(scaled_df)

    return merged_df, pair_plot