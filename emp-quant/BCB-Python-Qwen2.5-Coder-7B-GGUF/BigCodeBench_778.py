
from collections import defaultdict
from operator import itemgetter
from itertools import groupby

def task_func(news_articles):
    # Check if all articles have the required keys
    required_keys = {'title', 'title_url', 'id', 'category'}
    for article in news_articles:
        if not required_keys.issubset(article.keys()):
            raise ValueError("All articles must have the keys 'title', 'title_url', 'id', and 'category'.")

    # Sort articles by 'category' and then by 'title'
    sorted_articles = sorted(news_articles, key=itemgetter('category', 'title'))

    # Group articles by 'category'
    grouped_articles = defaultdict(list)
    for article in sorted_articles:
        grouped_articles[article['category']].append(article)

    return grouped_articles