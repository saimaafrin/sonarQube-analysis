import re
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np
def task_func(df):
    # Filter articles by their titles for specific case-insensitive keywords
    how_or_what_regex = re.compile(r"(how|what)", re.IGNORECASE)
    filtered_articles = df[df["title"].str.contains(how_or_what_regex)]

    # Vectorize the content using CountVectorizer
    vectorizer = CountVectorizer()
    vectorized_content = vectorizer.fit_transform(filtered_articles["content"])

    # Group articles into clusters using KMeans clustering
    kmeans = KMeans(n_clusters=3)
    cluster_labels = kmeans.fit_predict(vectorized_content)

    return cluster_labels
df = pd.DataFrame({"title": ["How to cook a meal", "What is the meaning of life?", "How to solve a problem", "What is the capital of France?"],
                   "content": ["This is a sample content for the first article.", "This is a sample content for the second article.", "This is a sample content for the third article.", "This is a sample content for the fourth article."]})