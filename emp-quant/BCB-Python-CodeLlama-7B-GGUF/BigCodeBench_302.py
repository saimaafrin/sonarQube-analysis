
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Constants
COLUMNS = ['Date', 'Value']
def task_func(df, plot=False):
    # Check if the input DataFrame is empty or has invalid 'Value'
    if df.empty or not df['Value'].apply(lambda x: isinstance(x, list)):
        raise ValueError("Invalid input DataFrame or 'Value' column")
    
    # Split the lists in the 'Value' column into separate columns
    df_split = pd.DataFrame(df['Value'].apply(pd.Series))
    df_split.columns = df_split.columns.str.split('_').str[0]
    
    # Calculate the Pearson correlation coefficient between the columns
    corr = df_split.corr()
    
    # Optionally, visualize the correlation matrix using a heatmap
    if plot:
        sns.heatmap(corr, annot=True, cmap='coolwarm', cbar=False, xticklabels=corr.columns, yticklabels=corr.columns)
        plt.title("Correlation Heatmap")
        plt.show()
    
    return corr