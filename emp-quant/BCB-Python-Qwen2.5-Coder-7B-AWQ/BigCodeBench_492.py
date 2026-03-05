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
        raise ValueError("epoch_milliseconds must be a non-negative integer")
    if not isinstance(random_seed, int):
        raise ValueError("random_seed must be an integer")
    if not isinstance(products, list) or len(products) != 5:
        raise ValueError("products must be a list of 5 strings")

    # Set random seed for reproducibility
    random.seed(random_seed)

    # Convert epoch time to datetime
    start_date = datetime.fromtimestamp(epoch_milliseconds / 1000)

    # Get current date
    end_date = datetime.now()

    # Initialize an empty list to store sales data
    sales_data = []

    # Generate sales data for each day
    current_date = start_date
    while current_date <= end_date:
        for product in products:
            # Generate random sales quantity
            sales_quantity = random.randint(10, 50)
            # Append sales data to the list
            sales_data.append({
                'Product': product,
                'Date': current_date,
                'Sales': sales_quantity
            })
        # Move to the next day
        current_date += pd.Timedelta(days=1)

    # Create a DataFrame from the sales data
    df = pd.DataFrame(sales_data)

    return df