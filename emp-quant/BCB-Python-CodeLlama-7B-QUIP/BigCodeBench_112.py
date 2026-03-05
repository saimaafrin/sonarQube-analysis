
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df):
    # Check if 'df' is a pandas DataFrame and if it contains the 'Status' column
    if not isinstance(df, pd.DataFrame) or 'Status' not in df:
        raise ValueError("'df' must be a pandas DataFrame with a 'Status' column")

    # Create a pie chart of the status distribution
    pie = df['Status'].value_counts().plot.pie(ylabel='Status')

    # Return the plot object
    return pie