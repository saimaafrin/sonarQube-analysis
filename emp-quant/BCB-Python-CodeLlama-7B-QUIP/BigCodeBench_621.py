
from itertools import chain
import numpy as np
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

def task_func(L):
    # Convert the list of lists to a list of integers
    L = [int(x) for x in L]

    # Standardize the integers
    scaler = StandardScaler()
    L = scaler.fit_transform(L)

    # Plot the standardized values
    fig, ax = plt.subplots()
    ax.plot(L)
    ax.set_xlabel("Standardized values")
    ax.set_ylabel("Values")
    ax.set_title("Standardized values")
    return ax