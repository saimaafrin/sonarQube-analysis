
from random import randint
from statistics import mean
import pandas as pd

def task_func(products_list):
    data = {'Product': products_list}
    for month in range(1, 13):
        data[f'Month {month}'] = [randint(10, 100) for _ in products_list]
    
    data['Average Sales'] = data.iloc[:, 1:].mean(axis=1)
    
    df = pd.DataFrame(data)
    return df