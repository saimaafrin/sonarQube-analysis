
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def task_func(rows=3, columns=2, seed=42):
    np.random.seed(seed)
    random_matrix = np.random.rand(rows, columns)
    scaler = MinMaxScaler()
    scaled_matrix = scaler.fit_transform(random_matrix)
    return scaled_matrix