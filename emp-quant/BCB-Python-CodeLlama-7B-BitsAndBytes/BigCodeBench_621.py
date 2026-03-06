
from itertools import chain
import numpy as np
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

def task_func(L):
    # Convert list of lists to a single list of integers
    flat_list = list(chain.from_iterable(L))

    # Standardize the integers
    scaler = StandardScaler()
    standardized_values = scaler.fit_transform(flat_list)

    # Plot the standardized values
    plt.plot(standardized_values)
    plt.xlabel('Index')
    plt.ylabel('Standardized Value')
    plt.title('Standardized Values')
    plt.show()