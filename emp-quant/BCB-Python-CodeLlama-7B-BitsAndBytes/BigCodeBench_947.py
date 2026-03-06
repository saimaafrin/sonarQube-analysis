
import numpy as np
import random
from datetime import datetime

def task_func(rows=3, columns=2, start_date=datetime(2021, 1, 1), end_date=datetime(2021, 12, 31), seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)

    # Initialize an empty list to store the dates
    dates = []

    # Generate the dates between the start and end date
    for i in range(rows):
        for j in range(columns):
            # Generate a random date between the start and end date
            date = random.randint(start_date.timestamp(), end_date.timestamp())
            # Convert the timestamp to a datetime object
            date = datetime.fromtimestamp(date)
            # Add the date to the list
            dates.append(date)

    # Convert the list to a numpy array
    dates_array = np.array(dates)

    # Reshape the array to the desired shape
    dates_array = dates_array.reshape((rows, columns))

    return dates_array