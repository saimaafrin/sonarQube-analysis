
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df):
    # Check if the input is a pandas DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input 'df' must be a pandas DataFrame")
    
    # Check if the DataFrame contains the 'Status' column
    if 'Status' not in df.columns:
        raise ValueError("Input DataFrame must contain the 'Status' column")
    
    # Draw the pie chart
    fig, ax = plt.subplots()
    ax.pie(df['Status'].value_counts(), labels=df['Status'].value_counts().index, autopct='%1.1f%%')
    
    # Return the Axes object
    return ax