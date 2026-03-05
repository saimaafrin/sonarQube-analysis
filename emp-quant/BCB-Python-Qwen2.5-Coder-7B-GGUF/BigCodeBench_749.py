
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def task_func(myList):
    scaler = MinMaxScaler()
    normalized_values = scaler.fit_transform(np.array(myList).reshape(-1, 1))
    return normalized_values.flatten()