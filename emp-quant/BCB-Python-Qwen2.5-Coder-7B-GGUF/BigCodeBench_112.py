
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df):
    # Check if df is a pandas DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame")
    
    # Check if 'Status' column exists in the DataFrame
    if 'Status' not in df.columns:
        raise ValueError("DataFrame must contain a 'Status' column")
    
    # Create a pie chart of the status distribution
    status_counts = df['Status'].value_counts()
    plot = status_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140)
    
    # Set the title of the pie chart
    plot.set_title('Status Distribution')
    
    # Return the Axes object with the pie chart
    return plot