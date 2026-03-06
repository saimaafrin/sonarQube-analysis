
import pandas as pd
from datetime import datetime
import random

def task_func(
    epoch_milliseconds,
    random_seed=0,
    products=["Product1", "Product2", "Product3", "Product4", "Product5"],
):
    # Check if the input epoch_milliseconds is valid
    try:
        datetime.fromtimestamp(epoch_milliseconds / 1000)
    except ValueError:
        raise ValueError("Invalid epoch milliseconds provided.")
    
    # Set the random seed for reproducibility
    random.seed(random_seed)
    
    # Convert epoch milliseconds to datetime object
    start_date = datetime.fromtimestamp(epoch_milliseconds / 1000)
    end_date = datetime.now()
    
    # Initialize an empty list to store the sales data
    sales_data = []
    
    # Generate sales data for each day between start_date and end_date
    current_date = start_date
    while current_date <= end_date:
        for product in products:
            sales_quantity = random.randint(10, 50)
            sales_data.append({
                'Product': product,
                'Date': current_date,
                'Sales': sales_quantity
            })
        current_date += timedelta(days=1)
    
    # Create a DataFrame from the sales data
    df = pd.DataFrame(sales_data)
    
    return df