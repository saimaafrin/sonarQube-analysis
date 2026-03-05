
import random
import pandas as pd
import numpy as np

def task_func(n,
          domain="samplewebsite.com",
          categories=['Sports', 'Technology', 'Health', 'Science', 'Business'],
          random_seed=None):
    if random_seed:
        random.seed(random_seed)
    articles = []
    for i in range(n):
        article = {
            "title": "Article " + str(i),
            "title_url": domain + "/Article_" + str(i),
            "id": i,
            "category": random.choice(categories),
            "views": np.random.poisson(1000)
        }
        articles.append(article)
    return pd.DataFrame(articles)