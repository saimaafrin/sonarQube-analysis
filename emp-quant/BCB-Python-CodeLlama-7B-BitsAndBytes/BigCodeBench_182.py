
import re
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import CountVectorizer

def task_func(df):
    # Filter articles with titles containing "how" or "what"
    how_what_articles = df[df['title'].str.lower().str.contains('how|what')]

    # Vectorize the content using CountVectorizer
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(how_what_articles['content'])

    # Perform KMeans clustering on the vectorized content
    kmeans = KMeans(n_clusters=3)
    kmeans.fit(X)

    # Get the cluster labels for the filtered articles
    cluster_labels = kmeans.labels_

    return cluster_labels