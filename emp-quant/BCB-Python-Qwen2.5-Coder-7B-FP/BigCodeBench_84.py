import numpy as np
import pandas as pd
def task_func(products, n_samples=100, sales_lower=50, sales_upper=200, profit_margin_min=0.1, profit_margin_max=0.5, random_seed=42):
    # Validate input types and values
    if not isinstance(products, list) or not all(isinstance(p, str) for p in products):
        raise TypeError("products must be a list of strings")
    if not isinstance(n_samples, int) or n_samples <= 0:
        raise ValueError("n_samples must be a positive integer")
    if not isinstance(sales_lower, (int, float)) or not isinstance(sales_upper, (int, float)) or sales_lower > sales_upper:
        raise ValueError("sales_lower must be less than or equal to sales_upper")
    if not isinstance(profit_margin_min, (int, float)) or not isinstance(profit_margin_max, (int, float)) or profit_margin_min > profit_margin_max:
        raise ValueError("profit_margin_min must be less than or equal to profit_margin_max")
    
    # Set random seed for reproducibility
    np.random.seed(random_seed)
    
    # Initialize a dictionary to store aggregated data
    aggregated_data = {product: {'sales': [], 'profit': []} for product in products}
    
    # Simulate sales and profit data for each product
    for _ in range(n_samples):
        for product in products:
            sales = np.random.randint(sales_lower, sales_upper + 1)
            profit_margin = np.random.uniform(profit_margin_min, profit_margin_max)
            profit = sales * profit_margin
            aggregated_data[product]['sales'].append(sales)
            aggregated_data[product]['profit'].append(profit)
    
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame.from_dict(aggregated_data, orient='index')
    df['total_sales'] = df['sales'].apply(sum)
    df['total_profit'] = df['profit'].apply(sum)
    df = df[['total_sales', 'total_profit']]
    df.sort_values(by='total_profit', ascending=False, inplace=True)
    
    return df