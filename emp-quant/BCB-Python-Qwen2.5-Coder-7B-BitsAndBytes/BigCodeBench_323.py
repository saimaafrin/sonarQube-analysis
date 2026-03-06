
import re
import numpy as np
from collections import Counter
from sklearn.mixture import GaussianMixture

def task_func(text, num_gaussians=1, seed=42):
    if num_gaussians <= 0:
        raise ValueError("num_gaussians must be greater than 0")
    
    # Extract names not enclosed by square brackets
    names = re.findall(r'\b\w+\b', text)
    
    # Tokenize names into words
    words = [name.split() for name in names]
    all_words = [word for sublist in words for word in sublist]
    
    # Count the frequency of each word
    word_counts = Counter(all_words)
    
    # Check if num_gaussians is greater than the number of unique words
    if num_gaussians > len(word_counts):
        raise Exception("num_gaussians cannot be greater than the number of unique words")
    
    # Fit a mixture of Gaussian distributions to the word frequencies
    frequencies = list(word_counts.values())
    gmm = GaussianMixture(n_components=num_gaussians, random_state=seed).fit(np.array(frequencies).reshape(-1, 1))
    
    # Return the means and variances of the fitted Gaussians
    result = {
        'means': gmm.means_.flatten().tolist(),
        'variances': gmm.covariances_.flatten().tolist()
    }
    
    return result