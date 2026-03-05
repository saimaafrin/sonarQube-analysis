import re
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import CountVectorizer
def task_func(df):
    # Filter articles with titles containing 'how' or 'what'
    filtered_df = df[df['title'].str.contains(r'\b(how|what)\b', case=False, regex=True)]
    
    # Vectorize the content using CountVectorizer
    vectorizer = CountVectorizer(stop_words='english')
    X = vectorizer.fit_transform(filtered_df['content'])
    
    # Apply KMeans clustering
    kmeans = KMeans(n_clusters=2, random_state=42)
    cluster_labels = kmeans.fit_predict(X)
    
    return cluster_labels.tolist()