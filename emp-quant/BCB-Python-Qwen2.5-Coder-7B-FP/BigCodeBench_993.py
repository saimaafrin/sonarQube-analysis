import re
from scipy.stats import gaussian_kde
from scipy import linalg
import matplotlib.pyplot as plt
def task_func(text):
    # Split the text into words using regular expression to handle different delimiters
    words = re.findall(r'\b\w+\b', text)
    
    # Calculate the lengths of the words
    word_lengths = [len(word) for word in words]
    
    # Create a figure and a subplot
    fig, ax = plt.subplots()
    
    # Plot the histogram of word lengths
    ax.hist(word_lengths, bins='auto', density=True, alpha=0.6, color='g')
    
    # Calculate the kernel density estimate
    kde = gaussian_kde(word_lengths)
    
    # Generate x values for the KDE curve
    x = np.linspace(min(word_lengths), max(word_lengths), 100)
    
    # Plot the KDE curve
    ax.plot(x, kde(x), 'r-', label='KDE')
    
    # Add labels and title
    ax.set_xlabel('Word Length')
    ax.set_ylabel('Density')
    ax.set_title('Word Length Distribution')
    ax.legend()
    
    # Return the Axes object
    return ax