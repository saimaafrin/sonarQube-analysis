
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Constants defining the range of random integers and the size of the DataFrame
RANGE = 100
SIZE = 1000

def task_func():
    """
    Generates a DataFrame with two columns, 'X' and 'Y', each filled with random integers within a specified range,
    and plots these points using a scatter plot. The visualization is created using Seaborn on top of Matplotlib.
    """
    # Generate random integers for 'X' and 'Y' columns
    X = np.random.randint(0, RANGE, SIZE)
    Y = np.random.randint(0, RANGE, SIZE)
    
    # Create a DataFrame
    df = pd.DataFrame({'X': X, 'Y': Y})
    
    # Plot the DataFrame using Seaborn
    sns.scatterplot(data=df, x='X', y='Y')
    plt.title('Scatter Plot of Random Points')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
    
    return df