
import os
import pandas as pd
from dateutil.parser import parse
import matplotlib.pyplot as plt

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

    # Set the title and labels
    plt.title('Year Distribution')
    plt.xlabel('Year')
    plt.ylabel('Count')

    # Return the histogram plot object
    return plt.gca()

# Call the function and save the plot to a file
task_func().savefig('year_distribution.png')