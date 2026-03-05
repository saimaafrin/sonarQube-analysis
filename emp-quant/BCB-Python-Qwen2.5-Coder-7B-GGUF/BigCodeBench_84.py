
import numpy as np
import pandas as pd

def task_func(products, n_samples=100, sales_lower=50, sales_upper=200, profit_margin_min=0.1, profit_margin_max=0.5, random_seed=42):
    # Validate input parameters
    if not isinstance(n_samples, int) or n_samples <= 0:
        raise ValueError("n_samples must be a positive integer")
    if sales_lower > sales_upper:
        raise ValueError("sales_lower must be less than or equal to sales_upper")
    if not isinstance(products, list) or not all(isinstance(product, str) for product in products):
        raise TypeError("products must be a list of strings")
    if not all(isinstance(value, (int, float)) for value in [sales_lower, sales_upper, profit_margin_min, profit_margin_max]):
        raise TypeError("sales_lower, sales_upper, profit_margin_min, and profit_margin_max must be numeric")
    
    # Set random seed for reproducibility
    np.random.seed(random_seed)
    
    # Generate random sales and profit data
    sales_data = np.random.randint(sales_lower, sales_upper, size=(n_samples, len(products)))
    profit_margins = np.random.uniform(profit_margin_min, profit_margin_max, size=(n_samples, len(products)))
    profits_data = sales_data * profit_margins
    
    # Aggregate data by product
    aggregated_sales = np.sum(sales_data, axis=0)
    aggregated_profits = np.sum(profits_data, axis=0)
    
    # Create DataFrame
    df = pd.DataFrame({
        'Product': products,
        'Total Sales': aggregated_sales,
        'Total Profit': aggregated_profits
    })
    
    # Sort by total profit in descending order
    df = df.sort_values(by='Total Profit', ascending=False).reset_index(drop=True)
    
    return df