
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Constants
COLUMNS = ['A', 'B', 'C', 'D', 'E']

def task_func(a, b):
    # Generate random values for the DataFrame
    data = np.random.randint(0, 100, size=(len(a), len(b)))

    # Create a DataFrame with the random values
    df = pd.DataFrame(data, index=a, columns=COLUMNS)

    # Plot the DataFrame as a bar chart
    ax = df.plot(kind='bar', stacked=True)

    return ax

# Show the plot
plt.show()