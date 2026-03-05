
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df):
    # Check if 'df' is a DataFrame and has the required columns
    if not (isinstance(df, pd.DataFrame) and 'Date' in df.columns and 'Sales' in df.columns):
        raise ValueError("'df' must be a DataFrame with 'Date' and 'Sales' columns")

    # Create a new figure and axis
    fig, ax = plt.subplots()

    # Plot the line chart
    ax.plot(df['Date'], df['Sales'])

    # Set the axis labels
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales')

    # Return the axis object
    return ax