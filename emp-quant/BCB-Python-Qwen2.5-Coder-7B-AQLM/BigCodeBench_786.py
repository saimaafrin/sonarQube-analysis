
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
    
    data = []
    for _ in range(n):
        country = random.choice(countries)
        product = random.choice(products)
        sales = random.randint(1, 100)
        data.append([country, product, sales])
    
    df = pd.DataFrame(data, columns=['Country', 'Product', 'Sales'])
    
    if output_path:
        df.to_csv(output_path, index=False)
    
    return df