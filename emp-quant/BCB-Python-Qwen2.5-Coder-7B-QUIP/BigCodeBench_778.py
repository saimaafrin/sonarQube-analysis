
from collections import defaultdict
from operator import itemgetter
from itertools import groupby

def task_func(news_articles):
    # Check if all articles have the required keys
    required_keys = {'title', 'title_url', 'id', 'category'}
    if not all(required_keys <= set(article) for article in news_articles):
        raise ValueError("Each article must have 'title', 'title_url', 'id', and 'category' keys.")

    # Sort articles by 'category' and 'title'
    sorted_articles = sorted(news_articles, key=itemgetter('category', 'title'))

    # Group articles by 'category'
    grouped_articles = defaultdict(list)
    for category, articles in groupby(sorted_articles, key=itemgetter('category')):
        grouped_articles[category] = list(articles)

    return grouped_articles

sorted_articles = task_func(articles)
print(sorted_articles)