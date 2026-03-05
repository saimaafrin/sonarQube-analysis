
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def task_func(rows=3, columns=2, seed=42):
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate a random matrix with the specified dimensions
    random_matrix = np.random.rand(rows, columns)
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Scale the random matrix to the range [0, 1]
    scaled_matrix = scaler.fit_transform(random_matrix)
    
    # Return the scaled matrix
    return scaled_matrix