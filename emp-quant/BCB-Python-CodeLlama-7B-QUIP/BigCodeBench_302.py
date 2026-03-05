
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Constants
COLUMNS = ['Date', 'Value']
def task_func(df, plot=False):
    if df.empty:
        raise ValueError("Input DataFrame is empty")
    if not df['Value'].isnull().all():
        raise ValueError("Input DataFrame contains invalid 'Value' column")
    # Split the lists in the 'Value' column into separate columns
    for col in df.columns:
        if col in COLUMNS:
            df[col] = df[col].apply(lambda x: x[0] if isinstance(x, list) else x)
    # Calculate the Pearson correlation coefficient between the columns
    corr_df = df.corr(method='pearson')
    # Visualize the correlation matrix using a heatmap
    if plot:
        fig, ax = plt.subplots()
        sns.heatmap(corr_df, ax=ax, cmap='viridis', annot=True)
        ax.set_title('Correlation Heatmap')
        plt.show()
    return corr_df