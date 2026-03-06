
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler

def task_func(x, y, labels):
    # Scale the x and y arrays using the standard scaler
    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(x)
    y_scaled = scaler.fit_transform(y)

    # Create a figure and axis object
    fig, ax = plt.subplots()

    # Plot the scaled x and y arrays as separate series with labels
    ax.plot(x_scaled, label='x')
    ax.plot(y_scaled, label='y')

    # Set the labels and title of the plot
    ax.set_xlabel('Scaled x')
    ax.set_ylabel('Scaled y')
    ax.set_title('Scaled x and y arrays')

    # Return the figure object
    return fig

fig = task_func(x, y, labels)

# Show the plot
plt.show()