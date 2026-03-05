
from random import randint
import matplotlib.pyplot as plt
import numpy as np

def task_func(array_length=100):
    array1 = np.array([randint(0, 100) for i in range(array_length)])
    array2 = np.array([randint(0, 100) for i in range(array_length)])
    max_array1 = np.max(array1)
    max_array2 = np.max(array2)
    plt.figure(figsize=(10, 10))
    plt.plot(max_array1, max_array2, 'r-')
    plt.xlabel('Maximum Values')
    plt.ylabel('Maximum Values')
    plt.title('Maximum Values')
    plt.show()
    return plt.gca()