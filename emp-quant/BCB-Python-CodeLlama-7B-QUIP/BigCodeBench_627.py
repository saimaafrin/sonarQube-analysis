
from random import randint
from statistics import mean
import pandas as pd

def task_func(products_list):
    sales_data = {}
    for product in products_list:
        sales_data[product] = [randint(100, 1000) for i in range(12)]
    sales_data_df = pd.DataFrame(sales_data, columns=['Product', 'Month 1', 'Month 2', 'Month 3', 'Month 4', 'Month 5', 'Month 6', 'Month 7', 'Month 8', 'Month 9', 'Month 10', 'Month 11', 'Month 12'])
    sales_data_df['Average Sales'] = sales_data_df.apply(lambda x: mean(x))
    return sales_data_df