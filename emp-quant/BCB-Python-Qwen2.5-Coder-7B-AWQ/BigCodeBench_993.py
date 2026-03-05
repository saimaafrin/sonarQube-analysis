import re
from scipy.stats import gaussian_kde
from scipy import linalg
import matplotlib.pyplot as plt
def task_func(text):
    # Extract words from the text
    words = re.findall(r'\b\w+\b', text)
    
    # Calculate the lengths of the words
    word_lengths = [len(word) for word in words]
    
    # Create a figure and an axes object
    fig, ax = plt.subplots()
    
    # Plot the histogram of word lengths
    ax.hist(word_lengths, bins='auto', density=True, alpha=0.6, color='g')
    
    # Calculate the KDE of word lengths
    kde = gaussian_kde(word_lengths)
    
    # Generate a range of x values for the KDE curve
    x = np.linspace(min(word_lengths), max(word_lengths), 100)
    
    # Plot the KDE curve
    ax.plot(x, kde(x), color='r')
    
    # Set the title and labels
    ax.set_title('Word Length Distribution')
    ax.set_xlabel('Word Length')
    ax.set_ylabel('Density')
    
    # Return the axes object
    return ax