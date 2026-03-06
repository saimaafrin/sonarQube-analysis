
import numpy as np
import random
from sklearn.preprocessing import MinMaxScaler

def task_func(list_of_lists, seed=42):
    scaler = MinMaxScaler()
    for i, sublist in enumerate(list_of_lists):
        if not sublist:
            random.seed(seed)
            list_of_lists[i] = [random.randint(0, 100) for _ in range(5)]
        else:
            list_of_lists[i] = scaler.fit_transform(np.array(sublist).reshape(-1, 1)).flatten().tolist()
    return list_of_lists