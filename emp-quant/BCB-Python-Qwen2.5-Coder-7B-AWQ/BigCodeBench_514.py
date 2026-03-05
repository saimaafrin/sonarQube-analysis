import pandas as pd
import matplotlib.pyplot as plt
def task_func(array):
    # Create a DataFrame from the 2D list
    df = pd.DataFrame(array, columns=['A', 'B', 'C', 'D', 'E'])
    
    # Calculate the sum of each column
    column_sums = df.sum()
    
    # Plot the sum of each column
    ax = column_sums.plot(kind='bar')
    plt.xlabel('Columns')
    plt.ylabel('Sum')
    plt.title('Sum of Each Column')
    
    return df, ax