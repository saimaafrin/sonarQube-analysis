import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler
def task_func(df1, df2):
    # Merge the two dataframes on the 'id' column
    merged_df = pd.merge(df1, df2, on='id', how='outer')

    # Scale the numeric features from df1 to have a mean of 0 and standard deviation of 1
    scaler = StandardScaler()
    scaled_df = scaler.fit_transform(merged_df.select_dtypes(include=['number']))

    # Create a pair plot of the scaled features from df1
    pair_plot = sns.pairplot(scaled_df, hue='id')

    return merged_df, pair_plot
df1 = pd.DataFrame({'id': [1, 2, 3], 'x': [10, 20, 30], 'y': [100, 200, 300]})
df2 = pd.DataFrame({'id': [1, 2, 4], 'x': [10, 20, 40], 'y': [100, 200, 400]})