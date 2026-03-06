
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Constants defining the range of random integers and the size of the DataFrame
RANGE = 100
SIZE = 1000

def task_func():
    # Generate random integers for X and Y columns
    data = {
        'X': np.random.randint(0, RANGE, SIZE),
        'Y': np.random.randint(0, RANGE, SIZE)
    }
    
    # Create a DataFrame from the dictionary
    df = pd.DataFrame(data)
    
    # Plotting the scatter plot using Seaborn
    sns.scatterplot(x='X', y='Y', data=df)
    plt.title('Scatter Plot of Random Points')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
    
    return df