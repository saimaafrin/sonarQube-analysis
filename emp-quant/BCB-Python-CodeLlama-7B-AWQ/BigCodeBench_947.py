import numpy as np
import random
from datetime import datetime
def task_func(rows=3, columns=2, start_date=datetime(2021, 1, 1), end_date=datetime(2021, 12, 31), seed=0):
    """
    Generates a matrix of given dimensions (rows x columns) containing unique dates between a specified start date and end date.
    """
    np.random.seed(seed)
    dates = np.empty((rows, columns), dtype=datetime)
    for i in range(rows):
        for j in range(columns):
            dates[i, j] = start_date + np.random.randint(0, (end_date - start_date).days)
    return dates