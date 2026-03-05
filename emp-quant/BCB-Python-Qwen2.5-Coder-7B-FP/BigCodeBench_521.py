import pandas as pd
import matplotlib.pyplot as plt
def task_func(data_list):
    """
    Plots a line graph of student scores over multiple tests.
    
    Parameters:
    - data_list: A list of dictionaries. Each dictionary contains the name of a student (key) and their score (value).
    
    Returns:
    - ax: The Axes object with the plotted data.
    """
    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(data_list)
    
    # Set the index to be the student names
    df.set_index('student', inplace=True)
    
    # Plot the line graph
    ax = df.plot(kind='line', marker='o')
    
    # Set labels and title
    ax.set_xlabel('Test Number')
    ax.set_ylabel('Score')
    ax.set_title('Student Scores Over Multiple Tests')
    
    # Show the plot
    plt.show()
    
    return ax