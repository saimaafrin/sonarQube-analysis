import os
import pandas as pd
from dateutil.parser import parse
OUTPUT_DIR = './output'
def task_func(csv_path=os.path.join(OUTPUT_DIR, 'data.csv'), date_column='date'):
    """
    Read a CSV file, convert a column of date strings into datetime objects, and draw a histogram of the year distribution of these dates.
    """
    # Read the CSV file
    df = pd.read_csv(csv_path)

    # Convert the date column to datetime objects
    df[date_column] = pd.to_datetime(df[date_column])

    # Extract the year from the datetime objects
    df['year'] = df[date_column].dt.year

    # Draw a histogram of the year distribution
    fig, ax = plt.subplots()
    ax.hist(df['year'], bins=range(1900, 2023), alpha=0.5, label='Year distribution')
    ax.set_xlabel('Year')
    ax.set_ylabel('Frequency')
    ax.set_title('Year distribution of dates in {}'.format(csv_path))
    ax.legend()

    return fig