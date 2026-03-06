
import pandas as pd
import csv
import random

def task_func(
    n, 
    countries=['USA', 'UK', 'China', 'India', 'Germany'], 
    products=['Product A', 'Product B', 'Product C', 'Product D', 'Product E'], 
    output_path=None,
    random_seed=None):
    
    if random_seed is not None:
        random.seed(random_seed)
    
    data = {
        'Country': [random.choice(countries) for _ in range(n)],
        'Product': [random.choice(products) for _ in range(n)],
        'Sales': [random.randint(1, 100) for _ in range(n)]
    }
    
    df = pd.DataFrame(data)
    
    if output_path:
        df.to_csv(output_path, index=False)
    
    return df