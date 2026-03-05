import numpy as np
import pandas as pd
def task_func(products, n_samples=100, sales_lower=50, sales_upper=200, profit_margin_min=0.1, profit_margin_max=0.5, random_seed=42):
    """
    Generate a sales report with randomly simulated sales and profit data for a given list of products.
    The data is aggregated by product and sorted by total profit in descending order.
    The function should raise the exception for:
        ValueError: If n_samples is not a positive integer, or if sales_lower is greater than sales_upper.
        TypeError: If products is not a list of strings, or if sales_lower, sales_upper, profit_margin_min, or profit_margin_max are not numeric.
    The function should output with:
        pd.DataFrame: A DataFrame containing aggregated sales and profit data for each product, sorted by profit.
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
    if profit_margin_min > profit_margin_max:
        raise ValueError("profit_margin_min must be less than or equal to profit_margin_max")

    # Generate random sales and profit data
    np.random.seed(random_seed)
    sales_data = np.random.randint(sales_lower, sales_upper, size=(n_samples, len(products)))
    profit_data = np.random.uniform(profit_margin_min, profit_margin_max, size=(n_samples, len(products)))

    # Aggregate and sort data
    sales_agg = sales_data.sum(axis=0)
    profit_agg = profit_data.sum(axis=0)
    data = pd.DataFrame({"Product": products, "Sales": sales_agg, "Profit": profit_agg})
    data = data.sort_values(by="Profit", ascending=False)

    return data
products = ["Product A", "Product B", "Product C"]