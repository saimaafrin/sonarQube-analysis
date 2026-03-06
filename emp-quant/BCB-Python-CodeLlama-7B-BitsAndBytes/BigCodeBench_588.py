
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Constants defining the range of random integers and the size of the DataFrame
RANGE = 100
SIZE = 1000

def task_func():
    # Generate random integers within the specified range
    x = np.random.randint(low=0, high=RANGE, size=SIZE)
    y = np.random.randint(low=0, high=RANGE, size=SIZE)

    # Create a DataFrame with the generated integers
    df = pd.DataFrame({'X': x, 'Y': y})

    # Plot the points using a scatter plot
    sns.scatterplot(data=df, x='X', y='Y')

    # Show the plot
    plt.show()

# Call the function
task_func()