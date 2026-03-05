
from collections import defaultdict
from operator import itemgetter
from itertools import groupby

def task_func(news_articles):
    # Check if the input is a list of dictionaries
    if not isinstance(news_articles, list):
        raise ValueError("Input must be a list of dictionaries")

    # Create a dictionary to store the sorted articles
    sorted_articles = defaultdict(list)

    # Group the articles by category
    for article in news_articles:
        category = article["category"]
        sorted_articles[category].append(article)

    # Sort the articles within each category by title
    for category, articles in sorted_articles.items():
        sorted_articles[category] = sorted(articles, key=itemgetter("title"))

    return sorted_articles