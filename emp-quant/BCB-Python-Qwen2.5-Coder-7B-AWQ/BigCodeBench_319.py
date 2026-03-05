import re
import matplotlib.pyplot as plt
from nltk.probability import FreqDist
def task_func(example_str, top_n=30):
    # Remove text enclosed in square brackets
    cleaned_str = re.sub(r'\[.*?\]', '', example_str)
    
    # Tokenize the cleaned string into words
    words = re.findall(r'\b\w+\b', cleaned_str)
    
    # Create a frequency distribution of the words
    freq_dist = FreqDist(words)
    
    # Get the top_n most common words
    top_words = freq_dist.most_common(top_n)
    
    # Plot the frequency distribution
    fig, ax = plt.subplots()
    ax.bar([word for word, freq in top_words], [freq for word, freq in top_words])
    ax.set_xlabel('Words')
    ax.set_ylabel('Frequency')
    ax.set_title('Frequency Distribution of Words')
    
    return ax, dict(top_words)
example_str = "This is a test string [with some] words [to test] the function."
top_n = 5