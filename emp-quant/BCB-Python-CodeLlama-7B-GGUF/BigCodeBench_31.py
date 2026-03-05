
import nltk
from string import punctuation
import seaborn as sns
import matplotlib.pyplot as plt
# Constants
PUNCTUATION = set(punctuation)
def task_func(text):
    # Tokenize the text
    tokens = nltk.word_tokenize(text)
    # Filter out tokens that start with '$' but consist only of punctuation
    filtered_tokens = [token for token in tokens if token.startswith('$') and not set(token).issubset(PUNCTUATION)]
    # Count the frequency of each token
    token_freq = nltk.FreqDist(filtered_tokens)
    # Plot the frequency of each token
    sns.barplot(x=token_freq.keys(), y=token_freq.values())
    return plt.gca()