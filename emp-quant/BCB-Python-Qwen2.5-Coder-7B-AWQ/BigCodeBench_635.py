import re
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
def task_func(text, n=2):
    # Preprocessing the text
    text = re.sub(r'\W+', ' ', text).lower()
    words = text.split()
    words = [word for word in words if word not in stopwords.words('english')]
    words = [words[i] for i in range(len(words)) if i == 0 or words[i] != words[i-1]]
    
    # Creating a co-occurrence matrix
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(words)
    co_occurrence_matrix = X.T.dot(X)
    
    # Creating a DataFrame from the co-occurrence matrix
    df = pd.DataFrame(co_occurrence_matrix.toarray(), index=vectorizer.get_feature_names_out(), columns=vectorizer.get_feature_names_out())
    
    # Plotting the co-occurrence matrix
    fig, ax = plt.subplots(figsize=(10, 10))
    cax = ax.matshow(df, interpolation='nearest', cmap='Blues')
    fig.colorbar(cax)
    ax.set_title('Co-occurrence Matrix')
    ax.set_xlabel('Words')
    ax.set_ylabel('Words')
    
    return df, ax