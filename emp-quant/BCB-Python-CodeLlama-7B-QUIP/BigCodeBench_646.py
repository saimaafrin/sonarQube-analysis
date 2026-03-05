
import os
import pandas as pd
from dateutil.parser import parse
OUTPUT_DIR = './output'
def task_func(csv_path=os.path.join(OUTPUT_DIR, 'data.csv'), date_column='date'):
    # Read the CSV file
    df = pd.read_csv(csv_path)
    # Convert the date column to datetime objects
    df[date_column] = pd.to_datetime(df[date_column])
    # Create a histogram of the year distribution
    years = df[date_column].dt.year
    years.hist(bins=100)
    return years.hist