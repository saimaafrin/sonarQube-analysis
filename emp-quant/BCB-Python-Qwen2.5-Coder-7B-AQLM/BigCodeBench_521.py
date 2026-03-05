
import pandas as pd
import matplotlib.pyplot as plt

def task_func(data_list):
    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(data_list)
    
    # Set the index to the student names
    df.set_index('name', inplace=True)
    
    # Plot the line graph
    ax = df.plot(kind='line', marker='o')
    
    # Set the title and labels
    ax.set_title('Student Scores Over Tests')
    ax.set_xlabel('Test Number')
    ax.set_ylabel('Score')
    
    # Show the plot
    plt.show()
    
    # Return the Axes object
    return ax