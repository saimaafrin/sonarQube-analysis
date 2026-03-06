
import os
import pandas as pd
import matplotlib.pyplot as plt
from dateutil.parser import parse

OUTPUT_DIR = './output'

def task_func(csv_path=os.path.join(OUTPUT_DIR, 'data.csv'), date_column='date'):
    # Read the CSV file
    df = pd.read_csv(csv_path)

    # Convert the date column to datetime objects
    df[date_column] = pd.to_datetime(df[date_column])

    # Extract the year from the datetime objects
    years = df[date_column].dt.year

    # Create a histogram of the year distribution
    plt.hist(years, bins=range(1900, 2020))
    plt.xlabel('Year')
    plt.ylabel('Count')
    plt.title('Year Distribution')

    # Save the plot to a file
    plt.savefig(os.path.join(OUTPUT_DIR, 'year_distribution.png'))

    return plt.gca()

# Call the function and save the plot to a file
task_func()