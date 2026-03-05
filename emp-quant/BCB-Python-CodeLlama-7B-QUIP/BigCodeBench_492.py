
import pandas as pd
from datetime import datetime
import random

def task_func(
    epoch_milliseconds,
    random_seed=0,
    products=["Product1", "Product2", "Product3", "Product4", "Product5"],
):
    # Check input validity
    if not isinstance(epoch_milliseconds, int) or epoch_milliseconds < 0:
        raise ValueError("Epoch time must be a positive integer")
    if not isinstance(random_seed, int) or random_seed < 0:
        raise ValueError("Random seed must be a positive integer")
    if not isinstance(products, list) or len(products) != 5:
        raise ValueError("Products must be a list of length 5")

    # Set random seed
    random.seed(random_seed)

    # Generate sales data for each day between epoch time and current time
    current_time = datetime.now().timestamp() * 1000
    start_time = epoch_milliseconds
    end_time = current_time
    dates = pd.date_range(start=start_time, end=end_time, freq="D")
    sales = []
    for date in dates:
        product = random.choice(products)
        sales.append({
            "Product": product,
            "Date": date,
            "Sales": random.randint(10, 50)
        })

    # Return sales data as a DataFrame
    return pd.DataFrame(sales)