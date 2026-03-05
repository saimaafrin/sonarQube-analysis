
import pandas as pd
import seaborn as sns
from collections import Counter
from textblob import TextBlob
from matplotlib import pyplot as plt

def task_func(text, n, top_k):
    blob = TextBlob(text)
    n_grams = blob.ngrams(n)
    n_grams_count = Counter(n_grams)
    top_n_grams = n_grams_count.most_common(top_k)
    return top_n_grams

top_n_grams = task_func(text, n, top_k)

# Visualize the top n-grams
sns.barplot(top_n_grams)
plt.show()