
import numpy as np
import pandas as pd

def task_func(products, n_samples=100, sales_lower=50, sales_upper=200, profit_margin_min=0.1, profit_margin_max=0.5, random_seed=42):
    # Validate input parameters
    if not isinstance(n_samples, int) or n_samples <= 0:
        raise ValueError("n_samples must be a positive integer")
    if not isinstance(products, list) or not all(isinstance(p, str) for p in products):
        raise TypeError("products must be a list of strings")
    if not isinstance(sales_lower, (int, float)) or not isinstance(sales_upper, (int, float)):
        raise TypeError("sales_lower and sales_upper must be numeric")
    if not isinstance(profit_margin_min, (int, float)) or not isinstance(profit_margin_max, (int, float)):
        raise TypeError("profit_margin_min and profit_margin_max must be numeric")
    if sales_lower >= sales_upper:
        raise ValueError("sales_lower must be less than sales_upper")
    if profit_margin_min >= profit_margin_max:
        raise ValueError("profit_margin_min must be less than profit_margin_max")

    # Set random seed for reproducibility
    np.random.seed(random_seed)

    # Generate random sales and profit data
    sales = np.random.randint(sales_lower, sales_upper, size=n_samples)
    profit_margins = np.random.uniform(profit_margin_min, profit_margin_max, size=n_samples)

    # Calculate profit
    profits = sales * profit_margins

    # Create DataFrame
    data = {'product': products, 'sales': sales, 'profit': profits}
    df = pd.DataFrame(data)

    # Aggregate by product and calculate total profit
    aggregated_df = df.groupby('product').agg({'sales': 'sum', 'profit': 'sum'}).reset_index()

    # Sort by total profit in descending order
    aggregated_df = aggregated_df.sort_values(by='profit', ascending=False)

    return aggregated_df