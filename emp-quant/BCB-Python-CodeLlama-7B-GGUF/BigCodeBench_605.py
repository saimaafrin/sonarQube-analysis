
import pandas as pd
import matplotlib.pyplot as plt

def task_func(matrix):
    # Create a heatmap of the matrix using the 'hot' colormap
    ax = plt.imshow(matrix, cmap='hot', interpolation='nearest')

    # Set the title and labels of the plot
    ax.set_title('Heatmap of the Matrix')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')

    # Show the plot
    plt.show()