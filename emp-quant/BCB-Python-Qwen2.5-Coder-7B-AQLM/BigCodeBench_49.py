
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

# Constants
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

def task_func(timestamps):
    if not timestamps:
        raise ValueError("Input list of timestamps is empty.")
    
    # Convert timestamps to datetime objects
    datetimes = [datetime.fromtimestamp(ts) for ts in timestamps]
    
    # Create a DataFrame
    df = pd.DataFrame({
        'Timestamp': timestamps,
        'Datetime': datetimes
    })
    
    # Draw a histogram
    fig, ax = plt.subplots()
    ax.hist(df['Datetime'], bins=10, format=DATE_FORMAT)
    ax.set_xlabel('Datetime')
    ax.set_ylabel('Frequency')
    ax.set_title('Distribution of Datetime Objects')
    
    return df, ax