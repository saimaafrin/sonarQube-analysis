import numpy as np
import random
from datetime import datetime, timedelta
def task_func(rows=3, columns=2, start_date=datetime(2021, 1, 1), end_date=datetime(2021, 12, 31), seed=0):
    random.seed(seed)
    date_range = (end_date - start_date).days + 1
    if rows * columns > date_range:
        raise ValueError("The product of rows and columns cannot be greater than the number of days between start_date and end_date.")
    
    dates = [start_date + timedelta(days=i) for i in range(date_range)]
    random.shuffle(dates)
    dates = dates[:rows * columns]
    matrix = np.array(dates).reshape(rows, columns)
    return matrix
rows = 3
columns = 2
start_date = datetime(2021, 1, 1)
end_date = datetime(2021, 12, 31)
seed = 0