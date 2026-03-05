
import pandas as pd
from datetime import datetime
import random

def task_func(
    epoch_milliseconds,
    random_seed=0,
    products=["Product1", "Product2", "Product3", "Product4", "Product5"],
):
    # Check input validity
    if epoch_milliseconds < 0:
        raise ValueError("Epoch milliseconds must be non-negative")
    if random_seed < 0:
        raise ValueError("Random seed must be non-negative")
    if len(products) != 5:
        raise ValueError("Number of products must be 5")

    # Set random seed
    random.seed(random_seed)

    # Generate sales data for each product
    sales_data = []
    for product in products:
        for day in range(epoch_milliseconds, datetime.now().timestamp() * 1000, 86400000):
            sales_data.append({
                "Product": product,
                "Date": datetime.fromtimestamp(day / 1000),
                "Sales": random.randint(10, 50)
            })

    # Create DataFrame
    df = pd.DataFrame(sales_data)

    return df