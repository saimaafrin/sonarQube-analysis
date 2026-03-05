
import pandas as pd
import random

def task_func(product_list, categories, min_value=10, max_value=100):
    # Generate random data for the sales report
    data = {
        'Product': product_list,
        'Category': categories,
        'Quantity Sold': [random.randint(min_value, max_value) for _ in range(len(product_list))],
        'Revenue': [random.randint(min_value, max_value) for _ in range(len(product_list))]
    }
    
    # Create a DataFrame from the data
    sales_report = pd.DataFrame(data)
    
    return sales_report