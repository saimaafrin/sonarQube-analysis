import nltk
from string import punctuation
import seaborn as sns
import matplotlib.pyplot as plt
PUNCTUATION = set(punctuation)
def task_func(text):
    """
    Draw a bar chart of the frequency of words in a text beginning with the "$" character. Words that start with the '$' character but consist only of punctuation (e.g., '$!$' and '$.$') are not included in the frequency count.
    """
    # Tokenize the text
    tokens = nltk.word_tokenize(text)
    # Filter out punctuation tokens
    tokens = [token for token in tokens if token not in PUNCTUATION]
    # Filter out tokens that do not start with '$'
    tokens = [token for token in tokens if token.startswith('$')]
    # Count the frequency of each token
    token_counts = {}
    for token in tokens:
        if token not in token_counts:
            token_counts[token] = 1
        else:
            token_counts[token] += 1
    # Sort the tokens by frequency
    sorted_tokens = sorted(token_counts.items(), key=lambda x: x[1], reverse=True)
    # Plot the bar chart
    fig, ax = plt.subplots()
    ax.bar(range(len(sorted_tokens)), [count for token, count in sorted_tokens])
    ax.set_xticks(range(len(sorted_tokens)))
    ax.set_xticklabels([token for token, count in sorted_tokens])
    ax.set_ylabel('Frequency')
    ax.set_title('Frequency of words beginning with "$"')
    return ax
text = "This is a test text with some $words and $!$ and $$.$$"