from itertools import chain
import numpy as np
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
def task_func(L):
    """
    Convert a list of lists 'L' into a single list of integers, standardize the integers, and plot the standardized values.
    """
    # Convert list of lists to a single list of integers
    L_int = list(chain.from_iterable(L))

    # Standardize the integers
    scaler = StandardScaler()
    L_std = scaler.fit_transform(L_int.reshape(-1, 1))

    # Plot the standardized values
    plt.plot(L_std)
    plt.show()
L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]