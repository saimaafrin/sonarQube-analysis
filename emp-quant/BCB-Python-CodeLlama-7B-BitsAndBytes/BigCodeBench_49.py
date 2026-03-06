
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

# Constants
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

def task_func(timestamps):
    if not timestamps:
        raise ValueError("Input list of timestamps is empty.")

    # Convert Unix timestamps to datetime objects
    datetime_objects = [datetime.fromtimestamp(ts) for ts in timestamps]

    # Create a Pandas DataFrame with the original timestamps and datetime objects
    df = pd.DataFrame({'Timestamp': timestamps, 'Datetime': datetime_objects})

    # Draw a histogram of the datetime objects
    ax = df['Datetime'].hist(bins=10)

    return df, ax

# Display the histogram
plt.show()