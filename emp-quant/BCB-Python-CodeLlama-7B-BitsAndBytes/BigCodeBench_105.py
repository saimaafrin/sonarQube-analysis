
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def task_func(df):
    # Check if the dataframe is empty
    if df.empty:
        raise ValueError("The dataframe is empty")

    # Check if the required columns are missing
    required_columns = ['date', 'value1', 'value2']
    if not all(col in df.columns for col in required_columns):
        raise ValueError("Required columns are missing")

    # Check if the 'date' column is in datetime format
    if not pd.to_datetime(df['date']).is_datetime64:
        raise ValueError("'date' column is not in datetime format")

    # Convert the 'date' column to an ordinal format
    df['date'] = pd.to_datetime(df['date']).dt.to_period('D')

    # Create a correlation matrix
    corr_matrix = df.corr()

    # Generate a pair plot of the dataframe
    g = sns.PairGrid(corr_matrix, diag_sharey=False)
    g.map_upper(plt.scatter)
    g.map_lower(sns.heatmap)
    g.add_legend()

    # Set the title of the plot
    g.fig.suptitle('Correlation Matrix')

    # Return the figure and PairGrid objects
    return g.fig, g