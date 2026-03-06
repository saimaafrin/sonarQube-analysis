
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def task_func(df):
    # Check if the dataframe is empty
    if df.empty:
        raise ValueError("The dataframe is empty.")
    
    # Check if the required columns are present
    required_columns = ['date']
    if not all(col in df.columns for col in required_columns):
        raise ValueError("Required columns are missing.")
    
    # Convert 'date' column to datetime format
    try:
        df['date'] = pd.to_datetime(df['date'])
    except ValueError:
        raise ValueError("'date' column is not in datetime format.")
    
    # Convert 'date' column to ordinal format
    df['date_ordinal'] = df['date'].apply(lambda x: x.toordinal())
    
    # Create a correlation matrix
    corr_matrix = df.corr()
    
    # Generate a pair plot
    pair_plot = sns.pairplot(df)
    pair_plot.fig.suptitle('Pair Plot')
    
    return corr_matrix, pair_plot