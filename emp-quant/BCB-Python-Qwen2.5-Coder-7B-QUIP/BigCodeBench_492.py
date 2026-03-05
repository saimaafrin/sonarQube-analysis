
import pandas as pd
from datetime import datetime, timedelta
import random

def task_func(
    epoch_milliseconds,
    random_seed=0,
    products=["Product1", "Product2", "Product3", "Product4", "Product5"],
):
    # Convert epoch time to datetime
    start_time = datetime.fromtimestamp(epoch_milliseconds / 1000)
    
    # Set the random seed for reproducibility
    random.seed(random_seed)
    
    # Initialize an empty list to store the sales data
    sales_data = []
    
    # Generate sales data for each day between the start time and the current time
    current_time = datetime.now()
    while start_time <= current_time:
        # Generate random sales data for each product
        for product in products:
            sales = random.randint(10, 50)
            sales_data.append({
                'Product': product,
                'Date': start_time,
                'Sales': sales
            })
        # Move to the next day
        start_time += timedelta(days=1)
    
    # Convert the list of sales data to a DataFrame
    df = pd.DataFrame(sales_data)
    
    return df