import numpy as np
import random
from datetime import datetime
def task_func(rows=3, columns=2, start_date=datetime(2021, 1, 1), end_date=datetime(2021, 12, 31), seed=0):
    """
    Generates a matrix of given dimensions (rows x columns) containing unique dates between a specified start date and end date.
    """
    # Set random seed for reproducibility
    random.seed(seed)

    # Initialize empty matrix
    matrix = np.empty((rows, columns))

    # Generate unique dates between start and end date
    for i in range(rows):
        for j in range(columns):
            matrix[i, j] = random.randint(start_date.timestamp(), end_date.timestamp())

    # Convert to datetime objects
    matrix = np.array([datetime.fromtimestamp(x) for x in matrix])

    return matrix