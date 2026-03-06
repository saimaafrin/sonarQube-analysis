
import pandas as pd
import numpy as np
import itertools
from datetime import datetime, timedelta
import seaborn as sns

def task_func(df, fruits=None, days=None, seed=None, sales_lower_bound=1, sales_upper_bound=50):
    # Check if 'df' is a pandas DataFrame
    if not isinstance(df, pd.DataFrame):
        raise TypeError("'df' must be a pandas DataFrame")

    # Check if 'fruits' is a list of strings
    if not isinstance(fruits, list) or not all(isinstance(fruit, str) for fruit in fruits):
        raise ValueError("'fruits' must be a list of strings")

    # Check if 'days' is a list of integers
    if not isinstance(days, list) or not all(isinstance(day, int) for day in days):
        raise ValueError("'days' must be a list of integers")

    # Check if 'seed' is an integer
    if not isinstance(seed, int):
        raise ValueError("'seed' must be an integer")

    # Check if 'sales_lower_bound' is less than 'sales_upper_bound'
    if sales_lower_bound >= sales_upper_bound:
        raise ValueError("'sales_lower_bound' must be less than 'sales_upper_bound'")

    # Generate random sales data for each fruit over the specified range of days
    sales_data = {}
    for fruit in fruits:
        sales_data[fruit] = {}
        for day in days:
            sales_data[fruit][day] = np.random.randint(sales_lower_bound, sales_upper_bound, size=1)

    # Create a new DataFrame with the sales data
    df_sales = pd.DataFrame(sales_data)

    # Create a seaborn boxplot of the sales data
    g = sns.boxplot(data=df_sales)

    return df_sales, g

df_sales, g = task_func(df, fruits, days, seed, sales_lower_bound, sales_upper_bound)

print(df_sales)
print(g)