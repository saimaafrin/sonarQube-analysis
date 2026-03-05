from itertools import chain
import numpy as np
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
def task_func(L):
    # Convert list of lists to a single list of integers
    L = list(chain.from_iterable(L))

    # Standardize the integers
    scaler = StandardScaler()
    L_std = scaler.fit_transform(L)

    # Plot the standardized values
    fig, ax = plt.subplots()
    ax.plot(L_std)
    ax.set_xlabel('Index')
    ax.set_ylabel('Standardized Value')
    ax.set_title('Standardized Values')
    plt.show()
L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]