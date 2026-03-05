
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd

def task_func(data):
    # Convert data to a pandas DataFrame
    df = pd.DataFrame(data)

    # Set the x-axis labels
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    df['month'] = months

    # Set the y-axis label
    df['value'] = df['value'].astype(int)

    # Create the bar chart
    fig, ax = plt.subplots()
    ax.bar(df['month'], df['value'])

    # Set the title and labels
    ax.set_title(f'Monthly Data for {datetime.now().year}')
    ax.set_xlabel('Month')
    ax.set_ylabel('Value')

    # Return the Axes object
    return ax