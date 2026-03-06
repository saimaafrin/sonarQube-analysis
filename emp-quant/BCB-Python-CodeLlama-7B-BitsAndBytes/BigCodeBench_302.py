
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Constants
COLUMNS = ['Date', 'Value']

def task_func(df, plot=False):
    # Check if the input DataFrame is empty or has invalid 'Value' column
    if df.empty or 'Value' not in df.columns:
        raise ValueError('Invalid input DataFrame or "Value" column not found')

    # Split the lists in the 'Value' column into separate columns
    df_split = df['Value'].str.split(',', expand=True)

    # Calculate the Pearson correlation coefficient between the columns
    corr = df_split.corr()

    # Optionally, visualize the correlation matrix using a heatmap
    if plot:
        sns.heatmap(corr, annot=True, cmap='coolwarm', square=True, xticklabels=corr.columns, yticklabels=corr.columns)
        plt.title('Correlation Heatmap')
        plt.show()

    return corr