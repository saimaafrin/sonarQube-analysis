import pandas as pd
import matplotlib.pyplot as plt
def task_func(data_list):
    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(data_list)
    
    # Set the index to be the student names
    df.set_index('student', inplace=True)
    
    # Plot the line graph
    ax = df.plot(kind='line')
    
    # Set the labels and title
    ax.set_xlabel('Test Number')
    ax.set_ylabel('Score')
    ax.set_title('Student Scores Over Tests')
    
    # Return the Axes object
    return ax