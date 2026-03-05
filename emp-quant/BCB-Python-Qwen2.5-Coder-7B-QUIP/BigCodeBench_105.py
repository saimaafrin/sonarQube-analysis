
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def task_func(df):
    # Check if the dataframe is empty
    if df.empty:
        raise ValueError("The dataframe is empty.")
    
    # Check if the 'date' column exists and is in datetime format
    if 'date' not in df.columns:
        raise ValueError("The 'date' column is missing.")
    
    # Convert the 'date' column to ordinal format
    df['date'] = pd.to_datetime(df['date']).dt.date.astype('category').cat.codes
    
    # Create a correlation matrix
    corr_matrix = df.corr()
    
    # Create a heatmap for the correlation matrix
    fig1, ax1 = plt.subplots()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax1)
    ax1.set_title('Correlation Matrix')
    
    # Create a pair plot
    grid = sns.pairplot(df)
    
    return fig1, grid