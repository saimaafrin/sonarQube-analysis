
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def task_func(rows=3, columns=2, seed=42):
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate a matrix of random values
    random_matrix = np.random.rand(rows, columns)
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Scale the matrix to be between 0 and 1
    scaled_matrix = scaler.fit_transform(random_matrix)
    
    return scaled_matrix