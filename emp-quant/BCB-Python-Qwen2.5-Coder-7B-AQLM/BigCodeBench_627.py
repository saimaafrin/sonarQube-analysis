
from random import randint
from statistics import mean
import pandas as pd

def task_func(products_list):
    data = {}
    for product in products_list:
        sales_data = [randint(100, 1000) for _ in range(12)]
        data[product] = sales_data + [mean(sales_data)]
    
    df = pd.DataFrame(data)
    df = df.set_index('Product').rename_axis(None, axis=1)
    return df