
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler

def task_func(x, y, labels):
    # Scaling the x and y arrays independently
    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(x)
    y_scaled = scaler.fit_transform(y)

    # Plotting the scaled x and y arrays as separate series with labels
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x_scaled, label=labels[0])
    ax.plot(y_scaled, label=labels[1])
    ax.set_xlabel(labels[0])
    ax.set_ylabel(labels[1])
    ax.set_title(f"{labels[0]} vs {labels[1]}")
    return fig