
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(data):
    # Check if the input data is a 2D array
    if not isinstance(data, np.ndarray) or data.ndim != 2:
        raise ValueError("Input data must be a 2D array")

    # Calculate the average of each row
    avg = data.mean(axis=1)

    # Create a pandas DataFrame with the average column
    df = pd.DataFrame(avg, columns=["Average"])

    # Create a heatmap of the correlation matrix
    sns.heatmap(data.corr(), annot=True, cmap="viridis")

    # Show the heatmap
    plt.show()

    return df, ax