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
    
    # Initialize lists to store data
    product_names = []
    sales = []
    profits = []
    
    # Generate data for each product
    for product in products:
        for _ in range(n_samples):
            sale = np.random.randint(sales_lower, sales_upper + 1)
            profit_margin = np.random.uniform(profit_margin_min, profit_margin_max)
            profit = sale * profit_margin
            product_names.append(product)
            sales.append(sale)
            profits.append(profit)
    
    # Create DataFrame
    df = pd.DataFrame({
        'Product': product_names,
        'Sales': sales,
        'Profit': profits
    })
    
    # Aggregate by product and sort by total profit in descending order
    aggregated_df = df.groupby('Product').agg({'Sales': 'sum', 'Profit': 'sum'}).reset_index()
    aggregated_df = aggregated_df.sort_values(by='Profit', ascending=False)
    
    return aggregated_df