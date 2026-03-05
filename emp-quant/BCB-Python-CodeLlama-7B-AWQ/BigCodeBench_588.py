import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
RANGE = 100
SIZE = 1000
def task_func():
    # Generate random integers within the specified range
    x = np.random.randint(RANGE, size=SIZE)
    y = np.random.randint(RANGE, size=SIZE)

    # Create a DataFrame with the generated integers
    df = pd.DataFrame({'X': x, 'Y': y})

    # Plot the points using a scatter plot
    sns.scatterplot(data=df, x='X', y='Y')

    # Show the plot
    plt.show()