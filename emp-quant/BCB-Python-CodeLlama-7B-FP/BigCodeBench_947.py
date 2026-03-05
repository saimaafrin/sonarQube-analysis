import numpy as np
import random
from datetime import datetime
def task_func(rows=3, columns=2, start_date=datetime(2021, 1, 1), end_date=datetime(2021, 12, 31), seed=0):
    """
    Generates a matrix of given dimensions (rows x columns) containing unique dates between a specified start date and end date.
    """
    np.random.seed(seed)
    dates = np.array([])
    for i in range(rows):
        for j in range(columns):
            dates = np.append(dates, random.randint(start_date, end_date))
    return dates.reshape(rows, columns)