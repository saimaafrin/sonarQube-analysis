
import re
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def task_func(df):
    # Check if 'Title' and 'Content' columns exist in the DataFrame
    if 'Title' not in df.columns or 'Content' not in df.columns:
        return plt.subplots()

    # Filter articles with titles containing "how" or "what"
    filtered_df = df[df['Title'].str.contains('how|what', case=False, na=False)]

    # If no articles are found, return an empty plot
    if filtered_df.empty:
        return plt.subplots()

    # Initialize the TfidfVectorizer
    vectorizer = TfidfVectorizer()

    # Fit and transform the content of the filtered articles
    X = vectorizer.fit_transform(filtered_df['Content'])

    # Get the feature names
    feature_names = vectorizer.get_feature_names_out()

    # Get the TF-IDF scores
    tfidf_scores = X.toarray()

    # Calculate the average TF-IDF score for each feature
    avg_tfidf_scores = np.mean(tfidf_scores, axis=0)

    # Create a bar plot of the TF-IDF scores
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(feature_names)), avg_tfidf_scores, tick_label=feature_names, rotation=90)
    plt.xlabel('Features')
    plt.ylabel('TF-IDF Score')
    plt.title('TF-IDF Scores of Features in Articles with Titles Containing "how" or "what"')
    plt.xticks(rotation=90)
    plt.tight_layout()

    # Return the Axes object
    return plt.gca()