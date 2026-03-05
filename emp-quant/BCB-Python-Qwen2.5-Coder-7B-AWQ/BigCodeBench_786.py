import pandas as pd
import csv
import random
def task_func(
    n, 
    countries=['USA', 'UK', 'China', 'India', 'Germany'], 
    products=['Product A', 'Product B', 'Product C', 'Product D', 'Product E'], 
    output_path=None,
    random_seed=None):
    """
    Generates random sales data and returns it as a pandas DataFrame.
    
    Parameters:
    - n: Number of rows in the DataFrame.
    - countries: List of countries to sample from.
    - products: List of products to sample from.
    - output_path: Path to save the generated data as a CSV file.
    - random_seed: Seed for the random number generator for reproducibility.
    
    Returns:
    - DataFrame: A pandas DataFrame with the generated sales data.
    """
    if random_seed is not None:
        random.seed(random_seed)
    
    data = {
        'Country': random.choices(countries, k=n),
        'Product': random.choices(products, k=n),
        'Sales': random.randint(1, 100, n)
    }
    
    df = pd.DataFrame(data)
    
    if output_path:
        df.to_csv(output_path, index=False)
    
    return df