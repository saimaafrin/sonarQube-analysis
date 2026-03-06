
import re
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def task_func(df):
    # Check if 'Title' and 'Content' columns exist in the DataFrame
    if 'Title' not in df.columns or 'Content' not in df.columns:
        return plt.figure()

    # Filter articles with titles containing "how" or "what"
    filtered_df = df[(df['Title'].str.contains('how', case=False)) | (df['Title'].str.contains('what', case=False))]

    # If no such articles are found, return an empty plot
    if filtered_df.empty:
        return plt.figure()

    # Initialize TfidfVectorizer
    vectorizer = TfidfVectorizer()
    
    # Fit and transform the content of the filtered articles
    tfidf_matrix = vectorizer.fit_transform(filtered_df['Content'])
    
    # Get feature names
    feature_names = vectorizer.get_feature_names_out()
    
    # Sum up the TF-IDF scores for each word across all articles
    tfidf_scores = np.sum(tfidf_matrix.toarray(), axis=0)
    
    # Create a bar plot
    fig, ax = plt.subplots()
    ax.barh(feature_names, tfidf_scores)
    
    # Set the y-axis label
    ax.set_ylabel('TF-IDF Score')
    
    # Rotate xtick labels for better readability
    plt.xticks(rotation=90)
    
    return ax