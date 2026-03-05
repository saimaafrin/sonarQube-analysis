import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def task_func(df):
    # Check if the dataframe is empty
    if df.empty:
        raise ValueError("The dataframe is empty.")
    
    # Check if required columns are missing
    required_columns = ['date', 'value1', 'value2']
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Required columns are missing: {', '.join(missing_columns)}")
    
    # Check if 'date' column is in datetime format
    if not pd.api.types.is_datetime64_any_dtype(df['date']):
        raise ValueError("The 'date' column is not in datetime format.")
    
    # Convert 'date' column to ordinal format
    df['date'] = df['date'].dt.toordinal()
    
    # Create a correlation matrix
    correlation_matrix = df.corr()
    
    # Generate a pair plot
    pair_plot = sns.pairplot(df)
    
    # Set the title of the plot
    pair_plot.fig.suptitle('Correlation Matrix')
    
    return correlation_matrix, pair_plot