
import re
import numpy as np
from collections import Counter
from sklearn.mixture import GaussianMixture

def task_func(text, num_gaussians=1, seed=42):
    # Check if num_gaussians is less than or equal to 0
    if num_gaussians <= 0:
        raise ValueError("num_gaussians must be greater than 0")
    
    # Extract names from the string that aren't enclosed by square brackets
    names = re.findall(r'\b\w+\b', text)
    
    # Tokenize the names into words
    words = [name.split() for name in names]
    words = [word for sublist in words for word in sublist]
    
    # Count the frequency of each word
    word_counts = Counter(words)
    
    # Check if num_gaussians is greater than the number of unique words
    if num_gaussians > len(word_counts):
        raise Exception("num_gaussians must be less than or equal to the number of unique words")
    
    # Fit a mixture of num_gaussians 1-D Gaussian distributions to the word frequencies
    gmm = GaussianMixture(n_components=num_gaussians, random_state=seed)
    gmm.fit(np.array(list(word_counts.values())).reshape(-1, 1))
    
    # Return the means and variances of the fitted Gaussians
    return {
        'means': gmm.means_.flatten().tolist(),
        'variances': gmm.covariances_.flatten().tolist()
    }