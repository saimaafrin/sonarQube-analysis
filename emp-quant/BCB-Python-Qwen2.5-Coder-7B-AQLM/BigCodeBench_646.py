
import os
import pandas as pd
from dateutil.parser import parse
import matplotlib.pyplot as plt
OUTPUT_DIR = './output'

def task_func(csv_path=os.path.join(OUTPUT_DIR, 'data.csv'), date_column='date'):
    # Ensure the output directory exists
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Read the CSV file
    df = pd.read_csv(csv_path)

    # Convert the date column to datetime objects
    df[date_column] = pd.to_datetime(df[date_column], errors='coerce')

    # Extract the year from the datetime objects
    df['year'] = df[date_column].dt.year

    # Create a histogram of the year distribution
    fig, ax = plt.subplots()
    ax.hist(df['year'].dropna(), bins=range(1900, 2021), edgecolor='black')
    ax.set_title('Year Distribution of Dates')
    ax.set_xlabel('Year')
    ax.set_ylabel('Frequency')

    return ax