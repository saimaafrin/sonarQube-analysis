
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Constants defining the range of random integers and the size of the DataFrame
RANGE = 100
SIZE = 1000
def task_func():
    # Generate random integers within the specified range
    x = np.random.randint(1, RANGE, SIZE)
    y = np.random.randint(1, RANGE, SIZE)
    # Create a DataFrame with the generated random integers
    df = pd.DataFrame({'X': x, 'Y': y})
    # Visualize the DataFrame using a scatter plot
    sns.scatterplot(x='X', y='Y', data=df)
    plt.show()
    return df