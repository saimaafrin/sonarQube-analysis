
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing

def task_func(original):
    # Normalize the array
    normalized = preprocessing.normalize(original)

    # Plot the original and normalized arrays
    fig, ax = plt.subplots()
    ax.plot(original, label='Original')
    ax.plot(normalized, label='Normalized')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    ax.legend()
    ax.set_title('Original vs. Normalized Data')
    return fig, ax

# Create a numeric array from the "original" list
original = np.array([1, 2, 3, 4, 5])

# Normalize the array
normalized = preprocessing.normalize(original)

# Plot the original and normalized arrays
fig, ax = task_func(original)

# Show the plot
plt.show()