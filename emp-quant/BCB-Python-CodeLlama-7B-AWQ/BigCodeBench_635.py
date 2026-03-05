import re
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
def task_func(text, n=2):
    """
    Analyzes a text string, removing duplicate consecutive words and stopwords defined by nltk.corpus, generates a square co-occurrence matrix of words, and plots this matrix.
    The function should output with:
        tuple:
        pd.DataFrame: Square co-occurrence matrix of words.
        matplotlib.axes.Axes: Plot object of the co-occurrence matrix.
    """
    # Remove duplicate consecutive words and stopwords
    text = re.sub(r'\s+', ' ', text)
    text = ' '.join([word for word in text.split() if word.lower() not in stopwords.words('english')])

    # Generate a square co-occurrence matrix of words
    vectorizer = CountVectorizer(ngram_range=(1, 1), min_df=0, max_df=1.0)
    X = vectorizer.fit_transform(text)
    co_occurrence_matrix = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names())

    # Plot the co-occurrence matrix
    fig, ax = plt.subplots(figsize=(10, 10))
    sns.heatmap(co_occurrence_matrix, ax=ax, cmap='coolwarm', vmin=0, vmax=1)
    ax.set_title('Co-occurrence Matrix')
    ax.set_xlabel('Word 1')
    ax.set_ylabel('Word 2')
    ax.set_xticks(np.arange(co_occurrence_matrix.shape[0]))
    ax.set_yticks(np.arange(co_occurrence_matrix.shape[1]))
    ax.set_xticklabels(co_occurrence_matrix.columns)
    ax.set_yticklabels(co_occurrence_matrix.index)
    plt.show()

    return co_occurrence_matrix, ax
text = "This is a sample text with some duplicate words and stopwords."