import pandas as pd
import matplotlib.pyplot as plt
def task_func(data_list):
    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(data_list)
    
    # Set the index to the student names
    df.set_index('name', inplace=True)
    
    # Plot the line graph
    ax = df.plot(kind='line', marker='o')
    
    # Set the labels and title
    ax.set_xlabel('Test Number')
    ax.set_ylabel('Score')
    ax.set_title('Student Scores Over Multiple Tests')
    
    # Show the plot
    plt.show()
    
    # Return the Axes object
    return ax