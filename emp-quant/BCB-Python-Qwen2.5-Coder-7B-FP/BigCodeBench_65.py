import pandas as pd
import matplotlib.pyplot as plt
COLUMNS = ['col1', 'col2', 'col3']
def task_func(data):
    # Convert the list of lists into a pandas DataFrame
    df = pd.DataFrame(data, columns=COLUMNS)
    
    # Group the DataFrame by all columns except the last one
    grouped = df.groupby(COLUMNS[:-1])
    
    # Calculate the mean of the last column for each group
    result_df = grouped[COLUMNS[-1]].mean().reset_index()
    
    # Create a line chart
    fig, ax = plt.subplots()
    for _, group in result_df.groupby(COLUMNS[:-1]):
        ax.plot(group[COLUMNS[:-1]], group[COLUMNS[-1]], marker='o')
    
    # Set the x-label and y-label
    x_label = '-'.join(COLUMNS[:-1])
    y_label = COLUMNS[-1]
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    
    return result_df, ax