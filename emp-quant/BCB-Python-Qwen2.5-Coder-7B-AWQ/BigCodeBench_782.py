import random
import pandas as pd
import numpy as np
def task_func(n,
              domain="samplewebsite.com",
              categories=['Sports', 'Technology', 'Health', 'Science', 'Business'],
              random_seed=None):
    if random_seed is not None:
        random.seed(random_seed)
    
    data = []
    for i in range(n):
        title = f"Article {i}"
        title_url = f"{domain}/Article_{i}"
        id = i
        category = random.choice(categories)
        views = np.random.poisson(lam=1000)
        data.append([title, title_url, id, category, views])
    
    df = pd.DataFrame(data, columns=['title', 'title_url', 'id', 'category', 'views'])
    return df