
import numpy as np
import random
from datetime import datetime

def task_func(rows=3, columns=2, start_date=datetime(2021, 1, 1), end_date=datetime(2021, 12, 31), seed=0):
    np.random.seed(seed)
    dates = np.random.randint(start_date, end_date, size=(rows, columns))
    return dates