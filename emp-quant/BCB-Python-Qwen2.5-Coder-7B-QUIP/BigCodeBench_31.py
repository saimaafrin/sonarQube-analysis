
import nltk
from string import punctuation
import seaborn as sns
import matplotlib.pyplot as plt
# Constants
PUNCTUATION = set(punctuation)

def task_func(text):
    # Tokenize the text into words
    words = nltk.word_tokenize(text)
    
    # Filter words that start with '$' and are not only punctuation
    filtered_words = [word for word in words if word.startswith('$') and not all(char in PUNCTUATION for char in word[1:])]
    
    # Count the frequency of each filtered word
    word_freq = nltk.FreqDist(filtered_words)
    
    # Check if there are any words that meet the criteria
    if not word_freq:
        return None
    
    # Plot the bar chart
    sns.barplot(x=word_freq.keys(), y=word_freq.values())
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title('Frequency of Words Starting with $')
    plt.show()
    
    return plt.gca()