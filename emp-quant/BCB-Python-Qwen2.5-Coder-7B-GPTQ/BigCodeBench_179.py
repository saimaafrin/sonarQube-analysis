import re
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
def task_func(df):
    # Check if 'Title' and 'Content' columns exist in the DataFrame
    if 'Title' not in df.columns or 'Content' not in df.columns:
        return plt.figure()

    # Filter articles with titles containing "how" or "what"
    filtered_df = df[df['Title'].str.contains(r'\b(how|what)\b', case=False, na=False)]

    # If no articles meet the criteria, return an empty plot
    if filtered_df.empty:
        return plt.figure()

    # Initialize TfidfVectorizer
    vectorizer = TfidfVectorizer()
    # Fit and transform the content of the filtered articles
    tfidf_matrix = vectorizer.fit_transform(filtered_df['Content'])
    # Get feature names
    feature_names = vectorizer.get_feature_names_out()

    # Sum the TF-IDF scores for each feature across all articles
    tfidf_scores = np.sum(tfidf_matrix.toarray(), axis=0)

    # Create a bar plot
    fig, ax = plt.subplots()
    ax.barh(feature_names, tfidf_scores, color='skyblue')
    ax.set_xlabel('TF-IDF Score')
    ax.set_yticks(feature_names)
    ax.set_yticklabels(feature_names, rotation=90, ha='right')

    return fig