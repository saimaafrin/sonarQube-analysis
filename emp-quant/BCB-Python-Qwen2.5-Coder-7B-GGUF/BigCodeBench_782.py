
import random
import pandas as pd
import numpy as np

def task_func(n,
              domain="samplewebsite.com",
              categories=['Sports', 'Technology', 'Health', 'Science', 'Business'],
              random_seed=None):
    if random_seed is not None:
        random.seed(random_seed)
        np.random.seed(random_seed)
    
    data = {
        'title': [f"Article_{i}" for i in range(n)],
        'title_url': [f"{domain}/Article_{i}" for i in range(n)],
        'id': list(range(n)),
        'category': [random.choice(categories) for _ in range(n)],
        'views': np.random.poisson(lam=1000, size=n)
    }
    
    df = pd.DataFrame(data)
    return df