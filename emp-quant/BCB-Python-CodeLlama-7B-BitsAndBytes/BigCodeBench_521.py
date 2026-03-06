
import pandas as pd
import matplotlib.pyplot as plt

def task_func(data_list):
    # Create a pandas DataFrame from the list of dictionaries
    df = pd.DataFrame(data_list)

    # Plot the line graph of student scores over tests
    ax = df.plot.line(x='test', y='score', kind='line')

    # Set the x-axis to be the test number
    ax.set_xlabel('Test Number')

    # Set the y-axis to be the score
    ax.set_ylabel('Score')

    # Set the title of the plot
    ax.set_title('Student Scores Over Tests')

    # Show the plot
    plt.show()

    return ax