import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
RANGE = 100
SIZE = 1000
def task_func():
    """
    Generates a DataFrame with two columns, 'X' and 'Y', each filled with random integers within a specified range,
    and plots these points using a scatter plot. The visualization is created using Seaborn on top of Matplotlib.
    
    Returns:
        pd.DataFrame: A DataFrame with 'X' and 'Y' columns containing the generated random integers.
    """
    # Generating random integers for 'X' and 'Y' columns
    data = {
        'X': np.random.randint(0, RANGE, SIZE),
        'Y': np.random.randint(0, RANGE, SIZE)
    }
    
    # Creating a DataFrame
    df = pd.DataFrame(data)
    
    # Plotting the DataFrame using Seaborn
    sns.scatterplot(data=df, x='X', y='Y')
    plt.show()
    
    return df