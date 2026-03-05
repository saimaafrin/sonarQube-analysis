
# Importing the required libraries
import re
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords

# Downloading the stopwords corpus if not already downloaded
try:
    nltk.corpus.stopwords.words('english')
except:
    nltk.download('stopwords')

def task_func(text, n=2):
    # Function to preprocess the text
    def preprocess(text):
        # Removing non-alphanumeric characters
        text = re.sub(r'[^a-zA-Z0-9 ]', '', text)
        # Converting to lowercase
        text = text.lower()
        # Removing stopwords
        stop_words = set(stopwords.words('english'))
        text = [word for word in text.split() if word not in stop_words]
        return ' '.join(text)

    # Preprocessing the text
    text = preprocess(text)

    # Splitting the text into words
    words = text.split()

    # Removing duplicate consecutive words
    words = [words[i] for i in range(len(words)) if i == 0 or words[i] != words[i-1]]

    # Creating a dictionary to count the co-occurrences
    co_occurrence = {}
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            if words[i] == words[j]:
                if (words[i], words[j]) not in co_occurrence:
                    co_occurrence[(words[i], words[j])] = 1
                else:
                    co_occurrence[(words[i], words[j])] += 1

    # Creating a DataFrame from the co-occurrence dictionary
    df = pd.DataFrame(list(co_occurrence.items()), columns=['Word1', 'Word2', 'Count'])

    # Creating a square co-occurrence matrix
    matrix = pd.pivot_table(df, values='Count', index='Word1', columns='Word2', fill_value=0)

    # Plotting the co-occurrence matrix
    fig, ax = plt.subplots()
    ax.imshow(matrix, cmap='viridis')
    ax.set_xlabel('Word2')
    ax.set_ylabel('Word1')
    ax.set_title('Co-occurrence Matrix')

    return df, ax