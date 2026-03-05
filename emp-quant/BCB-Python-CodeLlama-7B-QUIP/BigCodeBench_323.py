
import re
import numpy as np
from collections import Counter
from sklearn.mixture import GaussianMixture

def task_func(text, num_gaussians=1, seed=42):
    # Remove names that are enclosed by square brackets
    text = re.sub(r' \[.*?\]', '', text)
    # Tokenize the names into words
    words = re.split(r'\W+', text)
    # Count the frequency of each word
    counts = Counter(words)
    # Fit a mixture of num_gaussians 1-D Gaussian distributions to the word frequencies
    gmm = GaussianMixture(n_components=num_gaussians, random_state=seed)
    gmm.fit(counts.keys())
    # Return the means and variances of the fitted Gaussians
    return {word: (gmm.means_[i], gmm.covariances_[i]) for i, word in enumerate(gmm.means_)}