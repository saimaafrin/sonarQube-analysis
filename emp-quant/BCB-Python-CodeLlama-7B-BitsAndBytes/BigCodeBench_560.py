
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd

def task_func(data):
    # Create a pandas DataFrame from the data
    df = pd.DataFrame(data, columns=['month', 'value'])

    # Convert the 'month' column to datetime objects
    df['month'] = pd.to_datetime(df['month'], format='%Y-%m')

    # Group the DataFrame by month and calculate the mean of the 'value' column
    mean_df = df.groupby('month')['value'].mean()

    # Create a bar chart of the mean values
    ax = mean_df.plot(kind='bar', rot=0)

    # Set the title, x and y labels
    ax.set_title('Monthly Data for {}'.format(datetime.now().year))
    ax.set_xlabel('Month')
    ax.set_ylabel('Value')

    # Return the Axes object
    return ax