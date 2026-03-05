
import nltk
from string import punctuation
import seaborn as sns
import matplotlib.pyplot as plt
# Constants
PUNCTUATION = set(punctuation)

def task_func(text):
    # Tokenize the text into words
    words = nltk.word_tokenize(text)
    
    # Filter words that start with '$' and are not purely punctuation
    filtered_words = [word for word in words if word.startswith('$') and not all(char in PUNCTUATION for char in word)]
    
    # Count the frequency of each filtered word
    word_freq = nltk.FreqDist(filtered_words)
    
    # If no words meet the criteria, return None
    if not word_freq:
        return None
    
    # Create a bar chart using seaborn
    plt.figure(figsize=(10, 6))
    sns.barplot(x=word_freq.keys(), y=word_freq.values())
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title('Frequency of Words Beginning with $')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Return the axes object
    return plt.gca()