
import pandas as pd
import matplotlib.pyplot as plt

def task_func(array):
    # Create a DataFrame from the 2D list
    df = pd.DataFrame(array, columns=['A', 'B', 'C', 'D', 'E'])
    
    # Calculate the sum of each column
    column_sums = df.sum()
    
    # Plot the sum of each column
    fig, ax = plt.subplots()
    ax.bar(range(1, len(column_sums) + 1), column_sums, tick_label=df.columns)
    ax.set_xlabel('Columns')
    ax.set_ylabel('Sum')
    ax.set_title('Sum of Each Column')
    
    return df, ax