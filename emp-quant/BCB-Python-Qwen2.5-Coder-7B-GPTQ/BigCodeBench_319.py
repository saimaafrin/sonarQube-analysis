import re
import matplotlib.pyplot as plt
from nltk.probability import FreqDist
def task_func(example_str, top_n=30):
    # Remove text enclosed in square brackets
    cleaned_str = re.sub(r'\[.*?\]', '', example_str)
    
    # Tokenize the cleaned string into words
    words = cleaned_str.split()
    
    # Create a frequency distribution of the words
    freq_dist = FreqDist(words)
    
    # Get the top_n most common words
    top_words = freq_dist.most_common(top_n)
    
    # Plot the frequency distribution
    freq_dist.plot(top_n, cumulative=False)
    
    # Return the Axes object and the dictionary of top_n words
    return plt.gca(), dict(top_words)
example_str = "This is a test string [with some] words [to test] the function."