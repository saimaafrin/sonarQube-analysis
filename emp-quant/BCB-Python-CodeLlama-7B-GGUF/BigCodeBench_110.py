
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df):
    # Check if 'df' is a DataFrame and has the required columns
    if not isinstance(df, pd.DataFrame) or 'Date' not in df.columns or 'Sales' not in df.columns:
        raise ValueError("'df' must be a DataFrame with 'Date' and 'Sales' columns")

    # Check if 'df' has any data to plot
    if df.shape[0] == 0:
        raise ValueError("'df' has no data to plot")

    # Create the line chart
    fig, ax = plt.subplots()
    ax.plot(df['Date'], df['Sales'])
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales')
    ax.set_title('Daily Turnover Line Chart')

    return ax