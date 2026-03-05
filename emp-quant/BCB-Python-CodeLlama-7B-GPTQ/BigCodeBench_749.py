from sklearn.preprocessing import MinMaxScaler
import numpy as np
def task_func(myList):
    scaler = MinMaxScaler()
    normalized_list = scaler.fit_transform(myList.reshape(-1, 1))
    return normalized_list
myList = [1, 2, 3, 4, 5]