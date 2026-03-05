
import numpy as np
import random
from sklearn.preprocessing import MinMaxScaler

def task_func(list_of_lists, seed=42):
    scaler = MinMaxScaler()
    for i, sublist in enumerate(list_of_lists):
        if not sublist:
            random.seed(seed)
            sublist = [random.randint(0, 100) for _ in range(5)]
        list_of_lists[i] = scaler.fit_transform([sublist]).toarray()[0].tolist()
    return list_of_lists