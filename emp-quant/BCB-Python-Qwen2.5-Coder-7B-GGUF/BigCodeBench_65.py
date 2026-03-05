
import pandas as pd
import matplotlib.pyplot as plt
COLUMNS = ['col1', 'col2', 'col3']

def task_func(data):
    # Convert the list of lists into a pandas DataFrame
    df = pd.DataFrame(data, columns=COLUMNS)
    
    # Group the DataFrame by all columns except the last one and calculate the mean of the last column
    grouped_df = df.groupby(df.columns[:-1]).mean().reset_index()
    
    # Create a line chart
    fig, ax = plt.subplots()
    for name, group in grouped_df.groupby(COLUMNS[:-1].tolist()):
        ax.plot(group[COLUMNS[-1]], label='-'.join(map(str, name)))
    
    # Set the labels
    ax.set_xlabel('-'.join(COLUMNS[:-1]))
    ax.set_ylabel(COLUMNS[-1])
    
    # Add a legend
    ax.legend()
    
    return grouped_df, ax