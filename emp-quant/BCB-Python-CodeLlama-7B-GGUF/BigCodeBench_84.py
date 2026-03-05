
import numpy as np
import pandas as pd

def task_func(products, n_samples=100, sales_lower=50, sales_upper=200, profit_margin_min=0.1, profit_margin_max=0.5, random_seed=42):
    """
    Generate a sales report with randomly simulated sales and profit data for a given list of products.
    The data is aggregated by product and sorted by total profit in descending order.

    Parameters:
    products (list of strings): List of products to generate sales data for.
    n_samples (int, optional): Number of samples to generate for each product. Defaults to 100.
    sales_lower (int, optional): Lower bound for sales data. Defaults to 50.
    sales_upper (int, optional): Upper bound for sales data. Defaults to 200.
    profit_margin_min (float, optional): Minimum profit margin. Defaults to 0.1.
    profit_margin_max (float, optional): Maximum profit margin. Defaults to 0.5.
    random_seed (int, optional): Random seed for reproducibility. Defaults to 42.

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
        raise ValueError("n_samples must be a positive integer")
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

    # Generate random sales and profit data
    np.random.seed(random_seed)
    sales_data = np.random.randint(sales_lower, sales_upper, size=(len(products), n_samples))
    profit_data = np.random.uniform(profit_margin_min, profit_margin_max, size=(len(products), n_samples))

    # Calculate total profit for each product
    total_profit = sales_data * profit_data

    # Aggregate and sort data by total profit
    aggregated_data = pd.DataFrame(total_profit, index=products)
    aggregated_data.sort_values(by="total_profit", ascending=False, inplace=True)

    return aggregated_data