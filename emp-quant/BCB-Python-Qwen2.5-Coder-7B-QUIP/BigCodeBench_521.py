
import pandas as pd
import matplotlib.pyplot as plt

def task_func(data_list):
    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(data_list)
    
    # Pivot the DataFrame to have students as columns and tests as rows
    df_pivot = df.pivot(index='test', columns='student', values='score')
    
    # Plot the line graph
    ax = df_pivot.plot(legend=True, marker='o', figsize=(10, 6))
    
    # Set the plot title and labels
    ax.set_title('Student Scores Over Tests')
    ax.set_xlabel('Test Number')
    ax.set_ylabel('Score')
    
    # Show the plot
    plt.show()
    
    # Return the Axes object
    return ax