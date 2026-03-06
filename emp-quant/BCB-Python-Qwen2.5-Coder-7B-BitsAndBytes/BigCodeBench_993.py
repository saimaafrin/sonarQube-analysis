
import re
from scipy.stats import gaussian_kde
import matplotlib.pyplot as plt

def task_func(text):
    # Split the text into words
    words = re.findall(r'\b\w+\b', text)
    
    # Calculate the lengths of the words
    word_lengths = [len(word) for word in words]
    
    # Create a figure and an axes object
    fig, ax = plt.subplots()
    
    # Plot the histogram of word lengths
    ax.hist(word_lengths, bins='auto', density=True, alpha=0.6, color='g')
    
    # Check if there are enough data points to compute the KDE
    if len(word_lengths) > 1:
        # Compute the kernel density estimate
        kde = gaussian_kde(word_lengths)
        
        # Generate x values for plotting the KDE
        x_vals = np.linspace(min(word_lengths), max(word_lengths), 300)
        
        # Plot the KDE curve
        ax.plot(x_vals, kde(x_vals), 'r-', label='KDE')
    
    # Set labels and title
    ax.set_xlabel('Word Length')
    ax.set_ylabel('Frequency')
    ax.set_title('Distribution of Word Lengths')
    ax.legend()
    
    # Show the plot
    plt.show()
    
    return ax