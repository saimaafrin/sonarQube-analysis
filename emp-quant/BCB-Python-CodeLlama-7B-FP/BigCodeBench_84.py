import numpy as np
import pandas as pd
def task_func(products, n_samples=100, sales_lower=50, sales_upper=200, profit_margin_min=0.1, profit_margin_max=0.5, random_seed=42):
    """
    Generate a sales report with randomly simulated sales and profit data for a given list of products.
    The data is aggregated by product and sorted by total profit in descending order.
    """
    if not isinstance(products, list) or not all(isinstance(p, str) for p in products):
        raise TypeError("products must be a list of strings")
    if not isinstance(n_samples, int) or n_samples <= 0:
        raise ValueError("n_samples must be a positive integer")
    if sales_lower > sales_upper:
        raise ValueError("sales_lower must be less than or equal to sales_upper")
    if not isinstance(sales_lower, (int, float)) or not isinstance(sales_upper, (int, float)):
        raise TypeError("sales_lower and sales_upper must be numeric")
    if not isinstance(profit_margin_min, (int, float)) or not isinstance(profit_margin_max, (int, float)):
        raise TypeError("profit_margin_min and profit_margin_max must be numeric")
    if profit_margin_min > profit_margin_max:
        raise ValueError("profit_margin_min must be less than or equal to profit_margin_max")

    # Generate random sales and profit data for each product
    sales_data = []
    for product in products:
        sales = np.random.randint(sales_lower, sales_upper, size=n_samples)
        profit = sales * np.random.uniform(profit_margin_min, profit_margin_max, size=n_samples)
        sales_data.append({"product": product, "sales": sales, "profit": profit})

    # Aggregate and sort sales and profit data by product
    sales_profit_data = pd.DataFrame(sales_data)
    sales_profit_data = sales_profit_data.groupby("product").agg({"sales": "sum", "profit": "sum"})
    sales_profit_data = sales_profit_data.sort_values(by="profit", ascending=False)

    return sales_profit_data
products = ["Product A", "Product B", "Product C"]
n_samples = 100
sales_lower = 50
sales_upper = 200
profit_margin_min = 0.1
profit_margin_max = 0.5
random_seed = 42