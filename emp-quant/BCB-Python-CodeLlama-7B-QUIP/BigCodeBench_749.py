
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def task_func(myList):
    scaler = MinMaxScaler()
    normalized_values = scaler.fit_transform(myList)
    return normalized_values