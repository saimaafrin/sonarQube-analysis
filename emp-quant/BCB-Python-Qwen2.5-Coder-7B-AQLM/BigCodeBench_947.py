
import numpy as np
import random
from datetime import datetime, timedelta

def task_func(rows=3, columns=2, start_date=datetime(2021, 1, 1), end_date=datetime(2021, 12, 31), seed=0):
    random.seed(seed)
    date_range = (end_date - start_date).days + 1
    dates = [start_date + timedelta(days=i) for i in range(date_range)]
    random.shuffle(dates)
    matrix = np.array(dates[:rows * columns]).reshape(rows, columns)
    return matrix