
import pandas as pd
from datetime import datetime
import random

def task_func(epoch_milliseconds, random_seed=0, products=["Product1", "Product2", "Product3", "Product4", "Product5"]):
    # Check input validity
    if not isinstance(epoch_milliseconds, int):
        raise ValueError("epoch_milliseconds must be an integer")
    if not isinstance(random_seed, int):
        raise ValueError("random_seed must be an integer")
    if not isinstance(products, list):
        raise ValueError("products must be a list of strings")
    if len(products) != 5:
        raise ValueError("products must have 5 elements")

    # Set random seed
    random.seed(random_seed)

    # Generate sales data for each product for each day between epoch_milliseconds and current time
    sales_data = []
    current_time = datetime.now()
    for product in products:
        for day in range(int((current_time - datetime.fromtimestamp(epoch_milliseconds)).days)):
            sales_data.append({
                "Product": product,
                "Date": datetime.fromtimestamp(epoch_milliseconds) + timedelta(days=day),
                "Sales": random.randint(10, 50)
            })

    # Create a DataFrame from the sales data
    sales_df = pd.DataFrame(sales_data)

    return sales_df