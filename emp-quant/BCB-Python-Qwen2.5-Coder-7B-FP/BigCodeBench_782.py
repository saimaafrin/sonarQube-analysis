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
    
    titles = ['Article ' + str(i) for i in range(n)]
    title_urls = [domain + '/Article_' + str(i) for i in range(n)]
    ids = list(range(n))
    categories = random.choices(categories, k=n)
    views = np.random.poisson(lam=1000, size=n).tolist()
    
    df = pd.DataFrame({
        'title': titles,
        'title_url': title_urls,
        'id': ids,
        'category': categories,
        'views': views
    })
    
    return df