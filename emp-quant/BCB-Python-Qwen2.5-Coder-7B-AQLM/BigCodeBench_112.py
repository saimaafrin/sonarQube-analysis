
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df):
    if not isinstance(df, pd.DataFrame) or 'Status' not in df.columns:
        raise ValueError("Input must be a pandas DataFrame containing a 'Status' column.")
    
    # Count the occurrences of each status
    status_counts = df['Status'].value_counts()
    
    # Create a pie chart
    fig, ax = plt.subplots()
    ax.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=140)
    
    # Set the title
    ax.set_title('Status Distribution')
    
    return ax