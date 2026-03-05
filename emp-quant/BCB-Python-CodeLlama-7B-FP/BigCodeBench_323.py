import re
import numpy as np
from collections import Counter
from sklearn.mixture import GaussianMixture
def task_func(text, num_gaussians=1, seed=42):
    """
    Extract names from a string that aren't enclosed by square brackets, tokenize the names into words, and count the frequency of each word. Finally, fit a mixture of num_gaussians 1-D Gaussian distributions to the word frequencies and return the means and variances of the fitted Gaussians.
    """
    # Extract names from the text that aren't enclosed by square brackets
    names = re.findall(r'\[?\w+\]?', text)

    # Tokenize the names into words
    words = [word.split() for name in names for word in name.split()]

    # Count the frequency of each word
    word_counts = Counter(words)

    # Check if num_gaussians is valid
    if num_gaussians <= 0:
        raise ValueError("num_gaussians must be greater than 0")
    if num_gaussians > len(word_counts):
        raise ValueError("num_gaussians must be less than or equal to the number of unique words")

    # Fit a mixture of num_gaussians 1-D Gaussian distributions to the word frequencies
    gmm = GaussianMixture(n_components=num_gaussians, random_state=seed)
    gmm.fit(word_counts.values())

    # Return the means and variances of the fitted Gaussians
    return {
        'means': gmm.means_,
        'variances': gmm.covariances_
    }
text = "This is a sample text with names like [John Doe] and [Jane Smith]."