
import pandas as pd
from random import uniform

def task_func(n_data_points=1000, min_value=0.0, max_value=10.0, column_name='Value'):
    data = [uniform(min_value, max_value) for _ in range(n_data_points)]
    data = [round(x, 3) for x in data]
    df = pd.DataFrame({column_name: data})
    return df