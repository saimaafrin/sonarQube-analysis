
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
    for unique_value in grouped_df[COLUMNS[-1]].unique():
        subset = grouped_df[grouped_df[COLUMNS[-1]] == unique_value]
        ax.plot(subset[COLUMNS[:-1]], subset[COLUMNS[-1]], label=unique_value)
    
    # Set the x-label and y-label
    ax.set_xlabel('-'.join(COLUMNS[:-1]))
    ax.set_ylabel(COLUMNS[-1])
    
    # Add a legend
    ax.legend()
    
    return grouped_df, ax