
import random
import pandas as pd
import numpy as np

def task_func(n,
          domain="samplewebsite.com",
          categories=['Sports', 'Technology', 'Health', 'Science', 'Business'],
          random_seed=None):
    """
    Generate 'n' random articles with titles, URLs, IDs, categories, and views.
    """
    if random_seed is not None:
        random.seed(random_seed)

    # Initialize DataFrame with columns
    df = pd.DataFrame(columns=['title', 'title_url', 'id', 'category', 'views'])

    # Generate random article titles
    titles = [f"Article {i}" for i in range(n)]

    # Generate random article URLs
    urls = [f"{domain}/Article_{i}" for i in range(n)]

    # Generate random article IDs
    ids = [i for i in range(n)]

    # Generate random article categories
    categories = random.choices(categories, k=n)

    # Generate random article views using Poisson distribution with lambda=1000
    views = [np.random.poisson(1000) for _ in range(n)]

    # Add data to DataFrame
    df['title'] = titles
    df['title_url'] = urls
    df['id'] = ids
    df['category'] = categories
    df['views'] = views

    return df