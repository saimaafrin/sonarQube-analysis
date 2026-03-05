
import numpy as np
from sklearn.preprocessing import OneHotEncoder

def task_func(list_of_lists):
    one_hot = np.zeros((len(list_of_lists), len(list_of_lists[0])))
    for i in range(len(list_of_lists)):
        for j in range(len(list_of_lists[i])):
            one_hot[i][j] = list_of_lists[i][j]
    return one_hot