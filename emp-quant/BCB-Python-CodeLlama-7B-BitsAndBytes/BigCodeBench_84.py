
import numpy as np
import pandas as pd

def task_func(products, n_samples=100, sales_lower=50, sales_upper=200, profit_margin_min=0.1, profit_margin_max=0.5, random_seed=42):
    """
    Generate a sales report with randomly simulated sales and profit data for a given list of products.
    The data is aggregated by product and sorted by total profit in descending order.

    Parameters:
    products (list of strings): List of products to generate sales data for.
    n_samples (int): Number of samples to generate for each product.
    sales_lower (int): Lower bound for simulated sales data.
    sales_upper (int): Upper bound for simulated sales data.
    profit_margin_min (float): Minimum profit margin for simulated profit data.
    profit_margin_max (float): Maximum profit margin for simulated profit data.
    random_seed (int): Random seed for reproducibility.

    Returns:
    pd.DataFrame: A DataFrame containing aggregated sales and profit data for each product, sorted by profit.

    Raises:
    ValueError: If n_samples is not a positive integer, or if sales_lower is greater than sales_upper.
    TypeError: If products is not a list of strings, or if sales_lower, sales_upper, profit_margin_min, or profit_margin_max are not numeric.
    """

    # Check input parameters
    if not isinstance(products, list):
        raise TypeError("products must be a list of strings")
    if not all(isinstance(p, str) for p in products):
        raise TypeError("products must be a list of strings")
    if not isinstance(n_samples, int):
        raise TypeError("n_samples must be an integer")
    if n_samples <= 0:
        raise ValueError("n_samples must be a positive integer")
    if sales_lower > sales_upper:
        raise ValueError("sales_lower must be less than or equal to sales_upper")
    if not isinstance(sales_lower, (int, float)):
        raise TypeError("sales_lower must be a numeric value")
    if not isinstance(sales_upper, (int, float)):
        raise TypeError("sales_upper must be a numeric value")
    if not isinstance(profit_margin_min, (int, float)):
        raise TypeError("profit_margin_min must be a numeric value")
    if not isinstance(profit_margin_max, (int, float)):
        raise TypeError("profit_margin_max must be a numeric value")

    # Generate random sales and profit data for each product
    sales_data = {}
    for product in products:
        sales_data[product] = np.random.randint(sales_lower, sales_upper, size=n_samples)
        profit_data = sales_data[product] * np.random.uniform(profit_margin_min, profit_margin_max, size=n_samples)
        sales_data[product] = pd.Series(sales_data[product], name="Sales")
        profit_data = pd.Series(profit_data, name="Profit")
        sales_data[product] = pd.concat([sales_data[product], profit_data], axis=1)

    # Aggregate and sort data by total profit
    total_profit = sales_data.sum(axis=1)
    sales_data = sales_data.sort_values(by=total_profit, ascending=False)

    return sales_data