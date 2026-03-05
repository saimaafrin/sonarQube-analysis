
import nltk
from string import punctuation
import seaborn as sns
import matplotlib.pyplot as plt
# Constants
PUNCTUATION = set(punctuation)
def task_func(text):
    # Tokenize the text
    tokens = nltk.word_tokenize(text)
    # Remove punctuation
    tokens = [word for word in tokens if word not in PUNCTUATION]
    # Filter words starting with '$'
    filtered_words = [word for word in tokens if word.startswith('$')]
    # Count the frequency of each word
    word_freq = nltk.FreqDist(filtered_words)
    # Plot the bar chart
    ax = sns.barplot(x=word_freq.keys(), y=word_freq.values())
    return ax