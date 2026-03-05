
import numpy as np
import pandas as pd

def task_func(products, n_samples=100, sales_lower=50, sales_upper=200, profit_margin_min=0.1, profit_margin_max=0.5, random_seed=42):
    if not isinstance(products, list):
        raise TypeError("products must be a list of strings")
    if not isinstance(sales_lower, int) or sales_lower < 0:
        raise ValueError("sales_lower must be a positive integer")
    if not isinstance(sales_upper, int) or sales_upper < 0:
        raise ValueError("sales_upper must be a positive integer")
    if not isinstance(profit_margin_min, float) or profit_margin_min < 0 or profit_margin_min > 1:
        raise ValueError("profit_margin_min must be a float between 0 and 1")
    if not isinstance(profit_margin_max, float) or profit_margin_max < 0 or profit_margin_max > 1:
        raise ValueError("profit_margin_max must be a float between 0 and 1")
    if not isinstance(random_seed, int) or random_seed < 0:
        raise ValueError("random_seed must be a positive integer")

    np.random.seed(random_seed)
    sales = np.random.randint(sales_lower, sales_upper, size=n_samples)
    profits = np.random.rand(n_samples) * (profit_margin_max - profit_margin_min) + profit_margin_min
    df = pd.DataFrame({
        "product": products,
        "sales": sales,
        "profit": profits
    })
    df = df.groupby("product").agg({"sales": "sum", "profit": "sum"}).sort_values("profit", ascending=False)
    return df