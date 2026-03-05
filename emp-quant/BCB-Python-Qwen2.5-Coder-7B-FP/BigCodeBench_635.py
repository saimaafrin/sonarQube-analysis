import re
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
def task_func(text, n=2):
    # Tokenizing the text and removing stopwords
    words = re.findall(r'\b\w+\b', text.lower())
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    
    # Removing duplicate consecutive words
    words = [words[i] for i in range(len(words)) if i == 0 or words[i] != words[i-1]]
    
    # Creating a co-occurrence matrix
    vectorizer = CountVectorizer(vocabulary=words)
    X = vectorizer.fit_transform(words)
    co_occurrence_matrix = X.T.dot(X)
    
    # Converting the co-occurrence matrix to a DataFrame
    df = pd.DataFrame(co_occurrence_matrix.toarray(), index=words, columns=words)
    
    # Plotting the co-occurrence matrix
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.imshow(df, cmap='hot', interpolation='nearest')
    ax.set_xticks(np.arange(len(words)))
    ax.set_yticks(np.arange(len(words)))
    ax.set_xticklabels(words, rotation=90)
    ax.set_yticklabels(words)
    ax.set_title('Co-occurrence Matrix')
    plt.show()
    
    return df, ax