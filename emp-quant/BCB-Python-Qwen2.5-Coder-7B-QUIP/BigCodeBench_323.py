
import re
import numpy as np
from collections import Counter
from sklearn.mixture import GaussianMixture

def task_func(text, num_gaussians=1, seed=42):
    # Check if num_gaussians is within the allowed range
    if num_gaussians <= 0:
        raise ValueError("num_gaussians must be greater than 0")
    if num_gaussians > len(set(text.split())) - 1:
        raise ValueError("num_gaussians must be less than the number of unique words")

    # Extract names not enclosed by square brackets
    names = re.findall(r'\b\w+\b', text)

    # Tokenize the names into words
    words = re.findall(r'\b\w+\b', text)

    # Count the frequency of each word
    word_count = Counter(words)

    # Fit a mixture of Gaussian distributions to the word frequencies
    freqs = np.array(list(word_count.values()))
    gmm = GaussianMixture(n_components=num_gaussians, random_state=seed).fit(freqs.reshape(-1, 1))
    means = gmm.means_.flatten()
    covariances = gmm.covariances_.flatten()

    # Return the means and variances of the fitted Gaussians
    return {'means': means, 'variances': covariances}