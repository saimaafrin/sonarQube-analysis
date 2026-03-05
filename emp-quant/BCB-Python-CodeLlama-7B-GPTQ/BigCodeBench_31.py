import nltk
from string import punctuation
import seaborn as sns
import matplotlib.pyplot as plt
def task_func(text):
    """
    Draw a bar chart of the frequency of words in a text beginning with the "$" character. Words that start with the '$' character but consist only of punctuation (e.g., '$!$' and '$.$') are not included in the frequency count.
    """
    # Tokenize the text
    tokens = nltk.word_tokenize(text)
    # Filter out words that start with '$' but consist only of punctuation
    filtered_tokens = [token for token in tokens if token.startswith('$') and not token.isalpha()]
    # Count the frequency of remaining words
    word_freq = nltk.FreqDist(filtered_tokens)
    # Plot the frequency of words
    ax = sns.barplot(x=word_freq.keys(), y=word_freq.values())
    return ax
text = "This is a sample text with some $words$ and $!$punctuation$."