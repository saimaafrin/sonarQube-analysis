
import numpy as np
import random
from sklearn.preprocessing import MinMaxScaler

def task_func(list_of_lists, seed=42):
    scaler = MinMaxScaler()
    random.seed(seed)
    
    for i, sublist in enumerate(list_of_lists):
        if not sublist:
            list_of_lists[i] = [random.randint(0, 100) for _ in range(5)]
    
    scaled_lists = scaler.fit_transform(list_of_lists)
    return scaled_lists.tolist()