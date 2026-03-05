
# Importing the required libraries
import re
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords

def task_func(text, n=2):
    # Remove duplicate consecutive words
    text = re.sub(r'\b(\w+)(?=\s+\1)\b', '', text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    text = ' '.join([word for word in text.split() if word.lower() not in stop_words])
    
    # Generate co-occurrence matrix
    vectorizer = CountVectorizer(ngram_range=(1, n))
    X = vectorizer.fit_transform(text)
    co_occurrence_matrix = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names())
    
    # Plot co-occurrence matrix
    fig, ax = plt.subplots()
    sns.heatmap(co_occurrence_matrix, annot=True, ax=ax)
    ax.set_title('Co-occurrence Matrix')
    ax.set_xlabel('Word')
    ax.set_ylabel('Word')
    plt.show()
    
    return co_occurrence_matrix, ax