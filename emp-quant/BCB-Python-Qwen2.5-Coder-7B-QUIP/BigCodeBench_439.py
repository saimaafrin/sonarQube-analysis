
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(P, T):
    # Ensure P is a 2D matrix and T is a 3D tensor
    if not isinstance(P, np.ndarray) or not isinstance(T, np.ndarray):
        raise ValueError("Inputs must be numpy arrays.")
    if len(P.shape) != 2 or len(T.shape) != 3:
        raise ValueError("Inputs must have the correct dimensions.")
    
    # Perform matrix-tensor multiplication
    result = np.einsum('ij,klm->ikl', P, T)
    
    # Plot the result as a heatmap
    fig, ax = plt.subplots()
    sns.heatmap(result, annot=True, fmt="d", ax=ax)
    
    return result, ax