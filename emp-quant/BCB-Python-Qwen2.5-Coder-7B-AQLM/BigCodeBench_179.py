
import re
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def task_func(df):
    # Check if 'Title' and 'Content' columns exist
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

    # Get the maximum TF-IDF score for each feature
    max_tfidf_scores = np.max(tfidf_matrix.toarray(), axis=0)

    # Create a bar plot
    plt.figure(figsize=(10, 6))
    plt.barh(feature_names, max_tfidf_scores, color='skyblue')
    plt.xlabel('TF-IDF Score')
    plt.ylabel('Feature')
    plt.xticks(rotation=90)
    plt.title('TF-IDF Scores of Features in Articles with Titles Containing "how" or "what"')

    return plt.gca()