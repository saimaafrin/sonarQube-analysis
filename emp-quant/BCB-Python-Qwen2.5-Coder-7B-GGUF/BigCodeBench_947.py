
import numpy as np
import random
from datetime import datetime, timedelta

def task_func(rows=3, columns=2, start_date=datetime(2021, 1, 1), end_date=datetime(2021, 12, 31), seed=0):
    random.seed(seed)
    date_range = [start_date + timedelta(days=x) for x in range((end_date - start_date).days + 1)]
    random.shuffle(date_range)
    date_matrix = np.array(date_range[:rows*columns]).reshape(rows, columns)
    return date_matrix