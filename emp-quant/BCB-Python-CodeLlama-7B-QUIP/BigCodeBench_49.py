
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
# Constants
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
def task_func(timestamps):
    if len(timestamps) == 0:
        raise ValueError("Input list of timestamps is empty.")
    datetime_list = []
    for timestamp in timestamps:
        datetime_list.append(datetime.strptime(timestamp, DATE_FORMAT))
    datetime_df = pd.DataFrame({"Timestamp": timestamps, "Datetime": datetime_list})
    datetime_df.hist(bins=10)
    plt.show()
    return datetime_df