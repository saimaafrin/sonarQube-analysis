
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Constants
COLUMNS = ['Column1', 'Column2', 'Column3', 'Column4', 'Column5']

def task_func(rows):
    # Generate random integer values between 0 and 9 for each column
    data = np.random.randint(0, 10, size=(rows, len(COLUMNS)))

    # Create a Pandas DataFrame with the random data
    df = pd.DataFrame(data, columns=COLUMNS)

    # Count the non-zero values in each column
    non_zero_counts = df.count(axis=0)

    # Create a bar plot of the non-zero counts
    ax = non_zero_counts.plot(kind='bar')

    # Return the DataFrame and the Axes object
    return df, ax

# Call the function with a random number of rows
rows = np.random.randint(10, 20)
df, ax = task_func(rows)

# Show the plot
plt.show()