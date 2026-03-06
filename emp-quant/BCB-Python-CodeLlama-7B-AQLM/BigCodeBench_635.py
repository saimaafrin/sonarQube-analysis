import re
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
def task_func(text, n=2):
    """
    Analyzes a text string, removing duplicate consecutive words and stopwords defined by nltk.corpus,
    generates a square co-occurrence matrix of words, and plots this matrix.

    Parameters:
    - text (str): Input text to be analyzed.
    - n (int, optional): Size of n-grams for the co-occurrence matrix. Defaults to 2.

    Returns:
    - tuple:
        - pd.DataFrame: Square co-occurrence matrix of words.
        - matplotlib.axes.Axes: Plot object of the co-occurrence matrix.

    Requirements:
        - re
        - pandas
        - matplotlib.pyplot
        - numpy
        - sklearn.feature_extraction.text
        - nltk.corpus

    Example:
    >>> import matplotlib
    >>> text = "hello hello world world"
    >>> df, ax = task_func(text, n=2)
    >>> df.columns.tolist()
    ['hello world']
    >>> df.index.tolist()
    ['hello world']
    >>> df.iloc[0, 0]
    0
    >>> isinstance(ax, matplotlib.axes.Axes)
    True
    """
    # Removing duplicate consecutive words
    text = re.sub(r"(\w)\s+(\w)\s+", r"\1 \2", text)

    # Removing stopwords
    stop_words = set(stopwords.words("english"))
    text = " ".join([word for word in text.split() if word not in stop_words])

    # Creating a co-occurrence matrix
    vectorizer = CountVectorizer(ngram_range=(1, n))
    matrix = vectorizer.fit_transform(text.split())
    matrix = matrix.toarray()
    matrix = pd.DataFrame(matrix, columns=vectorizer.get_feature_names())

    # Plotting the co-occurrence matrix
    fig, ax = plt.subplots()
    ax.imshow(matrix, cmap="Blues")
    ax.set_xticks(np.arange(matrix.shape[1]))
    ax.set_yticks(np.arange(matrix.shape[0]))
    ax.set_xticklabels(matrix.columns, rotation=90)
    ax.set_yticklabels(matrix.index)
    ax.set_title("Co-occurrence matrix")
    ax.set_xlabel("Words")
    ax.set_ylabel("Words")
    ax.set_aspect(1)
    return matrix, ax