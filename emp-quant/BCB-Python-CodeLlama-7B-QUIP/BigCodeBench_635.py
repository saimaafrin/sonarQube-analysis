
# Importing the required libraries
import re
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords

def task_func(text, n=2):
    # Remove duplicate consecutive words
    text = re.sub(r"\s+", " ", text).strip()
    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    text = " ".join([word for word in text.split() if word not in stop_words])
    # Tokenize the text
    tokens = text.split()
    # Create a square co-occurrence matrix of words
    co_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            co_matrix[i, j] = len(set(tokens[i:j+1]))
    # Create a DataFrame from the co-occurrence matrix
    df = pd.DataFrame(co_matrix)
    # Plot the co-occurrence matrix
    fig, ax = plt.subplots()
    ax.imshow(df, cmap="gray")
    ax.set_xticks(np.arange(n))
    ax.set_yticks(np.arange(n))
    ax.set_xticklabels(df.index)
    ax.set_yticklabels(df.columns)
    ax.set_aspect("equal")
    plt.show()
    return df, ax