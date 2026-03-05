
import numpy as np
import matplotlib.pyplot as plt

def task_func(P, T):
    # Ensure the matrix P and tensor T are numpy arrays
    P = np.array(P)
    T = np.array(T)
    
    # Calculate the product using Einstein summation
    result = np.einsum('ij,ijk->ik', P, T)
    
    # Ensure the result has the expected shape (N, 3)
    if result.shape[1] != 3:
        raise ValueError("The result must have 3 elements along the second axis.")
    
    # Create a 3D plot of the result
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(range(len(result)), [0]*len(result), [0]*len(result), c=result, cmap='viridis')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    return result, ax