
import pandas as pd
import matplotlib.pyplot as plt

COLUMNS = ['col1', 'col2', 'col3']

def task_func(data):
    # Create DataFrame from the input data
    df = pd.DataFrame(data, columns=COLUMNS)
    
    # Group by all columns except the last one and calculate mean for the last column
    grouped_df = df.groupby(COLUMNS[:-1]).mean().reset_index()
    
    # Extract the x-label and y-label
    x_label = '-'.join(COLUMNS[:-1])
    y_label = COLUMNS[-1]
    
    # Plot the line chart
    fig, ax = plt.subplots()
    for key, group in grouped_df.groupby(COLUMNS[:-1]):
        ax.plot(group[COLUMNS[-1]], label='-'.join(map(str, key)))
    
    # Set labels
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    
    # Add legend
    ax.legend(title=x_label)
    
    return grouped_df, ax