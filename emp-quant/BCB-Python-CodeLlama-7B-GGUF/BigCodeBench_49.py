
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
# Constants
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
def task_func(timestamps):
    if not timestamps:
        raise ValueError("Input list of timestamps is empty.")
    datetime_list = [datetime.fromtimestamp(ts) for ts in timestamps]
    df = pd.DataFrame({"Timestamp": timestamps, "Datetime": datetime_list})
    ax = df.hist(bins=10, x="Datetime", y="Timestamp")
    return df, ax