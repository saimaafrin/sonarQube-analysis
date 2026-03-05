
import re
import numpy as np
from collections import Counter
from sklearn.mixture import GaussianMixture

def task_func(text, num_gaussians=1, seed=42):
    # Extract names from text that aren't enclosed by square brackets
    names = re.findall(r'\[?\w+\]?', text)

    # Tokenize names into words
    words = [name.split() for name in names]

    # Count frequency of each word
    word_freq = Counter(word for name in words for word in name)

    # Check if num_gaussians is valid
    if num_gaussians <= 0:
        raise ValueError("num_gaussians must be greater than 0")
    if num_gaussians > len(word_freq):
        raise ValueError("num_gaussians cannot be greater than the number of unique words")

    # Fit mixture of num_gaussians 1-D Gaussian distributions to word frequencies
    gmm = GaussianMixture(n_components=num_gaussians, random_state=seed)
    gmm.fit(word_freq.keys())

    # Return means and variances of fitted Gaussians
    return {
        'means': gmm.means_,
        'variances': gmm.covariances_
    }