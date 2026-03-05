
from random import randint
from statistics import mean
import pandas as pd

def task_func(products_list):
    sales_data = []
    for product in products_list:
        sales = []
        for month in range(1, 13):
            sales.append(randint(100, 1000))
        sales_data.append({
            'Product': product,
            'Month 1': sales[0],
            'Month 2': sales[1],
            'Month 3': sales[2],
            'Month 4': sales[3],
            'Month 5': sales[4],
            'Month 6': sales[5],
            'Month 7': sales[6],
            'Month 8': sales[7],
            'Month 9': sales[8],
            'Month 10': sales[9],
            'Month 11': sales[10],
            'Month 12': sales[11],
            'Average Sales': mean(sales)
        })
    return pd.DataFrame(sales_data)