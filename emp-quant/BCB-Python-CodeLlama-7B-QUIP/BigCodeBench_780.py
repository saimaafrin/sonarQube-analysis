
import pandas as pd
import pytz

def task_func(articles, timezone):
    # Convert 'published_time' to a specified timezone
    articles['published_time'] = pd.to_datetime(articles['published_time'], utc_tz=pytz.timezone(timezone))

    # Group articles by 'category'
    articles_grouped = articles.groupby('category')

    # Calculate the count, mean, min, max publication times only considering the hour
    count = articles_grouped.count()
    mean = articles_grouped.mean()
    min = articles_grouped.min()
    max = articles_grouped.max()

    # Create a DataFrame with the count, mean, min, max publication hour for each category
    data = pd.DataFrame({
        'category': articles_grouped.index,
        'count': count,
        'mean': mean,
        'min': min,
        'max': max
    })

    return data