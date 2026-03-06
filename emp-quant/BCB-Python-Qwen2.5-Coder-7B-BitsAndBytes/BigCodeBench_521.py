
import pandas as pd
import matplotlib.pyplot as plt

def task_func(data_list):
    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(data_list)
    
    # Set the index to be the 'name' column
    df.set_index('name', inplace=True)
    
    # Plot each student's scores over tests
    ax = df.plot(kind='line')
    
    # Set labels and title
    ax.set_xlabel('Test Number')
    ax.set_ylabel('Score')
    ax.set_title('Student Scores Over Multiple Tests')
    
    # Show the plot
    plt.show()
    
    return ax