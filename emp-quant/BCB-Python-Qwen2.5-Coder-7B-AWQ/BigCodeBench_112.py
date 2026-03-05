import pandas as pd
import matplotlib.pyplot as plt
def task_func(df):
    # Check if the input is a pandas DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input 'df' must be a pandas DataFrame.")
    
    # Check if the 'Status' column exists in the DataFrame
    if 'Status' not in df.columns:
        raise ValueError("The DataFrame must contain a 'Status' column.")
    
    # Count the occurrences of each status
    status_counts = df['Status'].value_counts()
    
    # Create a pie chart
    fig, ax = plt.subplots()
    ax.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=140)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    return ax