import pandas as pd
import matplotlib.pyplot as plt
def task_func(df):
    # Check if df is a pandas DataFrame and contains the 'Status' column
    if not isinstance(df, pd.DataFrame) or 'Status' not in df.columns:
        raise ValueError("Input must be a pandas DataFrame with a 'Status' column")
    
    # Group the data by 'Status' and count the occurrences
    status_counts = df['Status'].value_counts()
    
    # Create a pie chart
    fig, ax = plt.subplots()
    ax.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=140)
    
    # Set the title of the pie chart
    ax.set_title('Status Distribution')
    
    # Return the Axes object with the pie chart
    return ax