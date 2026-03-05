
import re
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import CountVectorizer

def task_func(df):
    # Filter articles with titles containing "how" or "what"
    how_what_articles = df[df['title'].str.lower().str.contains('how|what')]
    
    # Vectorize the content using CountVectorizer
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(how_what_articles['content'])
    
    # Perform KMeans clustering
    kmeans = KMeans(n_clusters=5)
    kmeans.fit(X)
    
    # Get cluster labels for the filtered articles
    cluster_labels = kmeans.labels_
    
    return cluster_labels