import pandas as pd
import matplotlib.pyplot as plt
def task_func(array):
    # Create a DataFrame from the 2D list
    df = pd.DataFrame(array, columns=['A', 'B', 'C', 'D', 'E'])
    
    # Calculate the sum of each column
    column_sums = df.sum()
    
    # Plot the sum of each column
    fig, ax = plt.subplots()
    column_sums.plot(kind='bar', ax=ax)
    ax.set_xlabel('Columns')
    ax.set_ylabel('Sum')
    ax.set_title('Sum of Each Column')
    
    return df, ax