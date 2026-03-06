
import pandas as pd
import matplotlib.pyplot as plt

def task_func(array):
    # Define the columns
    COLUMNS = ['A', 'B', 'C', 'D', 'E']
    
    # Create a DataFrame from the array
    df = pd.DataFrame(array, columns=COLUMNS)
    
    # Calculate the sum of each column
    sums = df.sum()
    
    # Plot the sums
    fig, ax = plt.subplots()
    sums.plot(kind='bar', ax=ax)
    ax.set_title('Sum of Each Column')
    ax.set_xlabel('Columns')
    ax.set_ylabel('Sum')
    
    return df, ax