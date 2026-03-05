import re
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
def task_func(text, n=2):
    # Remove duplicate consecutive words
    text = re.sub(r'\b(\w+)\s+\1\b', r'\1', text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    text = ' '.join([word for word in text.split() if word.lower() not in stop_words])

    # Generate a square co-occurrence matrix of words
    vectorizer = CountVectorizer(ngram_range=(1, 1))
    X = vectorizer.fit_transform(text)
    co_occurrence_matrix = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names())

    # Plot the co-occurrence matrix
    fig, ax = plt.subplots()
    sns.heatmap(co_occurrence_matrix, annot=True, cmap='Blues')
    ax.set_title('Co-occurrence Matrix')
    ax.set_xlabel('Word')
    ax.set_ylabel('Word')
    plt.show()

    return co_occurrence_matrix, ax
text = 'This is a sample text with some duplicate words and stopwords.'