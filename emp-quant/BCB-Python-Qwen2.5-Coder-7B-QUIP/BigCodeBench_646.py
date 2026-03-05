
import os
import pandas as pd
from dateutil.parser import parse
OUTPUT_DIR = './output'

def task_func(csv_path=os.path.join(OUTPUT_DIR, 'data.csv'), date_column='date'):
    # Read the CSV file
    df = pd.read_csv(csv_path)
    
    # Convert the date column to datetime objects
    df[date_column] = pd.to_datetime(df[date_column], errors='coerce', parser=parse)
    
    # Filter out the rows with valid datetime values
    df = df[df[date_column].notna()]
    
    # Extract the year from the datetime column
    df['year'] = df[date_column].dt.year
    
    # Draw a histogram of the year distribution
    fig, ax = plt.subplots()
    df['year'].value_counts().sort_index().plot(kind='bar', ax=ax)
    
    # Set the plot title and labels
    ax.set_title('Year Distribution of Dates')
    ax.set_xlabel('Year')
    ax.set_ylabel('Frequency')
    
    # Return the plot object
    return ax