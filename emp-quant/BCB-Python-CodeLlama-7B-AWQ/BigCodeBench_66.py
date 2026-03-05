import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
COLUMNS = ['col1', 'col2', 'col3']
def task_func(data):
    # Build a pandas DataFrame by using list of elements.
    df = pd.DataFrame(data, columns=COLUMNS)

    # Create a new dataframe by grouping the values in the column 'col3' by ['col1', 'col2'].
    grouped_df = df.groupby(['col1', 'col2'])['col3'].agg('count')

    # Reset the index of the newly created dataframe.
    grouped_df = grouped_df.reset_index()

    # Create a distribution plot of the 'col3' column of the previous dataframe using seaborn.
    sns.distplot(grouped_df['col3'], xlabel='col3')

    # Return the DataFrame and the seaborn plot object.
    return df, plt.gca()