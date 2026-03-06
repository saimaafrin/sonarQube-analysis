
import numpy as np
import pandas as pd

def task_func(products, n_samples=100, sales_lower=50, sales_upper=200, profit_margin_min=0.1, profit_margin_max=0.5, random_seed=42):
    # Validate input parameters
    if not isinstance(n_samples, int) or n_samples <= 0:
        raise ValueError("n_samples must be a positive integer")
    if sales_lower > sales_upper:
        raise ValueError("sales_lower must be less than or equal to sales_upper")
    if not all(isinstance(product, str) for product in products):
        raise TypeError("products must be a list of strings")
    if not (isinstance(sales_lower, (int, float)) and isinstance(sales_upper, (int, float))):
        raise TypeError("sales_lower and sales_upper must be numeric")
    if not (isinstance(profit_margin_min, (int, float)) and isinstance(profit_margin_max, (int, float))):
        raise TypeError("profit_margin_min and profit_margin_max must be numeric")

    # Set random seed for reproducibility
    np.random.seed(random_seed)

    # Generate random sales and profit data
    sales_data = {}
    for product in products:
        sales_data[product] = {
            'sales': np.random.randint(sales_lower, sales_upper + 1, n_samples),
            'profit_margin': np.random.uniform(profit_margin_min, profit_margin_max, n_samples)
        }

    # Calculate total profit for each product
    profit_data = {product: np.sum(data['sales'] * data['profit_margin']) for product, data in sales_data.items()}

    # Create DataFrame from profit data
    df = pd.DataFrame(list(profit_data.items()), columns=['Product', 'Total Profit'])

    # Sort DataFrame by total profit in descending order
    df.sort_values(by='Total Profit', ascending=False, inplace=True)

    return df