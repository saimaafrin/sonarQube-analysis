import pandas as pd
import matplotlib.pyplot as plt
def task_func(matrix):
    """
    Visualize a 2D numeric array (matrix) as a heatmap using matplotlib.

    Parameters:
    matrix (list of lists): A 2D numeric array to be visualized as a heatmap.

    Returns:
    ax (matplotlib.axes._axes.Axes): The Axes object with the heatmap.
    """
    # Convert the matrix to a pandas DataFrame
    df = pd.DataFrame(matrix)
    
    # Create a heatmap using matplotlib
    fig, ax = plt.subplots()
    heatmap = ax.imshow(df, cmap='hot', interpolation='nearest')
    
    # Add colorbar to the heatmap
    plt.colorbar(heatmap)
    
    # Return the Axes object
    return ax