
import pandas as pd
import matplotlib.pyplot as plt

def task_func(array):
    # Create a Pandas DataFrame from the 2D list
    df = pd.DataFrame(array, columns=['A', 'B', 'C', 'D', 'E'])

    # Calculate the sum of each column
    sums = df.sum(axis=0)

    # Create a matplotlib Axes object
    fig, ax = plt.subplots()

    # Plot the sum of each column
    ax.plot(sums)

    # Set the title and labels
    ax.set_title('Sum of each column')
    ax.set_xlabel('Column')
    ax.set_ylabel('Sum')

    # Return the DataFrame and Axes object
    return df, ax

# Show the plot
plt.show()