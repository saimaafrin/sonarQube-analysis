
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler

def task_func(x, y, labels):
    # Scale the x and y arrays independently
    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(x)
    y_scaled = scaler.fit_transform(y)

    # Plot the scaled arrays as separate series
    fig, ax = plt.subplots()
    ax.plot(x_scaled, label=labels[0])
    ax.plot(y_scaled, label=labels[1])

    # Set the labels and title
    ax.set_xlabel('Scaled x')
    ax.set_ylabel('Scaled y')
    ax.set_title('Scaled x and y')

    return fig