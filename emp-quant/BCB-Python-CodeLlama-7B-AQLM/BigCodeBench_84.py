import numpy as np
import pandas as pd
def task_func(products, n_samples=100, sales_lower=50, sales_upper=200, profit_margin_min=0.1, profit_margin_max=0.5, random_seed=42):
    """
    Generate a sales report with randomly simulated sales and profit data for a given list of products.
    The data is aggregated by product and sorted by total profit in descending order. 
    
    Parameters:
    - products (list of str): List of product names.
    - n_samples (int): The number of data points to generate for the report. Default is 100.
    - sales_lower (int): The minimum sales value for the random generation. Default is 50.
    - sales_upper (int): The maximum sales value for the random generation. Default is 200.
    - profit_margin_min (float): The minimum profit margin as a fraction of sales. Default is 0.1.
    - profit_margin_max (float): The maximum profit margin as a fraction of sales. Default is 0.5.
    - random_seed (int): Seed for the random number generator to ensure reproducibility. Default is 42.

    Returns:
    pd.DataFrame: A DataFrame containing aggregated sales and profit data for each product, sorted by profit.

    Raises:
    ValueError: If n_samples is not a positive integer, or if sales_lower is greater than sales_upper.
    TypeError: If products is not a list of strings, or if sales_lower, sales_upper, profit_margin_min, or profit_margin_max are not numeric.

    Requirements:
    - numpy
    - pandas

    Example:
    >>> products = ["iPhone", "iPad", "Macbook", "Airpods", "Apple Watch"]
    >>> report = task_func(products, n_samples=50, sales_lower=100, sales_upper=150, profit_margin_min=0.2, profit_margin_max=0.4, random_seed=42)
    >>> print(report)
           Product  Sales      Profit
    2      Macbook   1561  444.826709
    3         iPad   1383  401.925334
    0      Airpods   1297  381.482713
    1  Apple Watch   1123  308.078536
    4       iPhone    921  294.013887
    """
    # Check inputs
    if not isinstance(products, list):
        raise TypeError("products must be a list of strings")
    if not all(isinstance(product, str) for product in products):
        raise TypeError("products must be a list of strings")
    if not isinstance(n_samples, int):
        raise TypeError("n_samples must be an integer")
    if not isinstance(sales_lower, int):
        raise TypeError("sales_lower must be an integer")
    if not isinstance(sales_upper, int):
        raise TypeError("sales_upper must be an integer")
    if not isinstance(profit_margin_min, float):
        raise TypeError("profit_margin_min must be a float")
    if not isinstance(profit_margin_max, float):
        raise TypeError("profit_margin_max must be a float")
    if not isinstance(random_seed, int):
        raise TypeError("random_seed must be an integer")
    if n_samples <= 0:
        raise ValueError("n_samples must be a positive integer")
    if sales_lower > sales_upper:
        raise ValueError("sales_lower must be less than or equal to sales_upper")
    if profit_margin_min > profit_margin_max:
        raise ValueError("profit_margin_min must be less than or equal to profit_margin_max")

    # Generate random data
    np.random.seed(random_seed)
    sales = np.random.randint(sales_lower, sales_upper, n_samples)
    profit = np.random.uniform(profit_margin_min, profit_margin_max, n_samples) * sales

    # Generate report
    report = pd.DataFrame({"Product": products, "Sales": sales, "Profit": profit})
    report = report.groupby("Product").agg({"Sales": "sum", "Profit": "sum"}).sort_values("Profit", ascending=False)
    report.reset_index(inplace=True)
    return report