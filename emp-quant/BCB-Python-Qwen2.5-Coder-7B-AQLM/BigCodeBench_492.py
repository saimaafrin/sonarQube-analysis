
import pandas as pd
from datetime import datetime
import random

def task_func(
    epoch_milliseconds,
    random_seed=0,
    products=["Product1", "Product2", "Product3", "Product4", "Product5"],
):
    # Set the random seed for reproducibility
    random.seed(random_seed)
    
    # Convert epoch milliseconds to datetime
    start_date = datetime.fromtimestamp(epoch_milliseconds / 1000)
    end_date = datetime.now()
    
    # Initialize an empty list to store sales data
    sales_data = []
    
    # Generate sales data for each day between start_date and end_date
    current_date = start_date
    while current_date <= end_date:
        for product in products:
            sales = random.randint(10, 50)
            sales_data.append({'Product': product, 'Date': current_date, 'Sales': sales})
        current_date += timedelta(days=1)
    
    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(sales_data)
    
    return df