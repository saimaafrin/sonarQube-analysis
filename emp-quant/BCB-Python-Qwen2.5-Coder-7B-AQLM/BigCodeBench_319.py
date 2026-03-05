
import re
import matplotlib.pyplot as plt
from nltk.probability import FreqDist

def task_func(example_str, top_n=30):
    # Remove text enclosed in square brackets
    cleaned_str = re.sub(r'\[.*?\]', '', example_str)
    
    # Tokenize the cleaned string into words
    words = cleaned_str.split()
    
    # Create a frequency distribution of the words
    fdist = FreqDist(words)
    
    # Get the top_n most common words
    top_words = fdist.most_common(top_n)
    
    # Plot the frequency distribution
    fdist.plot(top_n, cumulative=False)
    
    # Return the plot and the top_n words dictionary
    return plt.gca(), dict(top_words)