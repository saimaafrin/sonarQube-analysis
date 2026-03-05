import re
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np
def task_func(df):
    # Filter articles by keywords
    how_or_what_re = re.compile(r"(how|what)", re.IGNORECASE)
    filtered_articles = df[df['title'].str.contains(how_or_what_re)]

    # Vectorize content
    vectorizer = CountVectorizer()
    vectorized_content = vectorizer.fit_transform(filtered_articles['content'])

    # Cluster articles
    kmeans = KMeans(n_clusters=3)
    cluster_labels = kmeans.fit_predict(vectorized_content)

    return cluster_labels
df = pd.DataFrame({
    'title': ['How to cook a cake', 'What is the meaning of life?', 'How to solve a math problem', 'What is the capital of France?'],
    'content': ['This is a sample article about how to cook a cake.', 'This is a sample article about what the meaning of life is.', 'This is a sample article about how to solve a math problem.', 'This is a sample article about what the capital of France is.']
})