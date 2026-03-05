
import pandas as pd
import matplotlib.pyplot as plt

def task_func(array):
    # Define the column names
    COLUMNS = ['A', 'B', 'C', 'D', 'E']
    
    # Create a DataFrame from the 2D list
    df = pd.DataFrame(array, columns=COLUMNS)
    
    # Calculate the sum of each column
    column_sums = df.sum()
    
    # Plot the sum of each column
    fig, ax = plt.subplots()
    column_sums.plot(kind='bar', ax=ax)
    ax.set_xlabel('Columns')
    ax.set_ylabel('Sum of Values')
    ax.set_title('Sum of Each Column')
    
    return df, ax