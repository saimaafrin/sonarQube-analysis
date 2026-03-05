import re
import numpy as np
from collections import Counter
from sklearn.mixture import GaussianMixture
def task_func(text, num_gaussians=1, seed=42):
    """
    Extract names from a string that aren't enclosed by square brackets, tokenize the names into words, and count the frequency of each word. Finally, fit a mixture of num_gaussians 1-D Gaussian distributions to the word frequencies and return the means and variances of the fitted Gaussians.
    The function should raise the exception for:
        ValueError: If num_gaussians is less than or equal to 0.
        Exception: If num_gaussians is greater than the number of unique words.
    The function should output with:
        dict: A dictionary with the frequency of each word.
    """
    # Extract names from the text that aren't enclosed by square brackets
    names = re.findall(r'\[?\w+\]?', text)

    # Tokenize the names into words
    words = [word for name in names for word in name.split()]

    # Count the frequency of each word
    word_counts = Counter(words)

    # Fit a mixture of num_gaussians 1-D Gaussian distributions to the word frequencies
    gmm = GaussianMixture(n_components=num_gaussians, random_state=seed)
    gmm.fit(word_counts.values())

    # Return the means and variances of the fitted Gaussians
    return {word: (gmm.means_[i], gmm.covariances_[i]) for i, word in enumerate(word_counts.keys())}
text = "This is a test string with names [John Doe] and [Jane Smith]."