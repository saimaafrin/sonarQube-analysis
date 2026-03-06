
import random
import pandas as pd
import numpy as np

def task_func(n,
          domain="samplewebsite.com",
          categories=['Sports', 'Technology', 'Health', 'Science', 'Business'],
          random_seed=None):
    # Set the random seed if provided
    if random_seed is not None:
        random.seed(random_seed)

    # Create a list of dictionaries to store the article data
    article_data = []

    # Generate 'n' random articles
    for i in range(n):
        # Generate a random title
        title = f"Article {i}"

        # Generate a random URL for the title
        url = f"{domain}/{title}"

        # Generate a random ID for the article
        id = i

        # Generate a random category for the article
        category = random.choice(categories)

        # Generate a random view count for the article
        views = np.random.poisson(1000)

        # Add the article data to the list of dictionaries
        article_data.append({
            "title": title,
            "title_url": url,
            "id": id,
            "category": category,
            "views": views
        })

    # Create a pandas DataFrame from the list of dictionaries
    df = pd.DataFrame(article_data)

    return df