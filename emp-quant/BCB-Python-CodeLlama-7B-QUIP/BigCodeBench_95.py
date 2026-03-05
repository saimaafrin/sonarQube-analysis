
import pandas as pd
from random import randint, uniform, seed

def task_func(categories=None, months=None, random_seed=42):
    if not categories or not months:
        raise ValueError("Please provide a list of categories and months")

    seed(random_seed)

    sales_data = []
    for category in categories:
        for month in months:
            sales_data.append({
                "Month": month,
                "Category": category,
                "Sales": randint(100, 500) + uniform(0, 1)
            })

    return pd.DataFrame(sales_data)