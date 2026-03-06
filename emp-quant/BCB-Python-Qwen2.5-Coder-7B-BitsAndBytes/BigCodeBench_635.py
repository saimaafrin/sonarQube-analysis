
# Importing the required libraries
import re
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords

def task_func(text, n=2):
    # Download necessary NLTK data if not already downloaded
    import nltk
    nltk.download('stopwords')
    
    # Tokenize the text and remove duplicates
    words = re.findall(r'\b\w+\b', text.lower())
    unique_words = list(dict.fromkeys(words))
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in unique_words if word not in stop_words]
    
    # Create a dictionary to store co-occurrences
    co_occurrence_dict = {word: {} for word in filtered_words}
    for i in range(len(filtered_words)):
        for j in range(i + 1, len(filtered_words)):
            if filtered_words[i] in text and filtered_words[j] in text:
                co_occurrence_dict[filtered_words[i]][filtered_words[j]] = text.count(f"{filtered_words[i]} {filtered_words[j]}")
                co_occurrence_dict[filtered_words[j]][filtered_words[i]] = text.count(f"{filtered_words[j]} {filtered_words[i]}")
    
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(index=filtered_words, columns=filtered_words)
    for word1 in filtered_words:
        for word2 in filtered_words:
            df.at[word1, word2] = co_occurrence_dict.get(word1, {}).get(word2, 0)
    
    # Plot the co-occurrence matrix
    fig, ax = plt.subplots(figsize=(10, 8))
    heatmap = ax.imshow(df, cmap='hot', interpolation='nearest')
    ax.set_xticks(np.arange(len(filtered_words)))
    ax.set_yticks(np.arange(len(filtered_words)))
    ax.set_xticklabels(filtered_words)
    ax.set_yticklabels(filtered_words)
    ax.figure.colorbar(heatmap)
    ax.set_title('Co-Occurrence Matrix')
    plt.show()
    
    return df, ax