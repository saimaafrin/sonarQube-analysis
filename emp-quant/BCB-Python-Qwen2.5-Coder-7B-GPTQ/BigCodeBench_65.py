import pandas as pd
import matplotlib.pyplot as plt
COLUMNS = ['col1', 'col2', 'col3']
def task_func(data):
    # Create a DataFrame from the input data
    df = pd.DataFrame(data, columns=COLUMNS)
    
    # Group the DataFrame by all columns except the last one
    grouped = df.groupby(df.columns[:-1]).size().reset_index(name='count')
    
    # Create a line chart
    fig, ax = plt.subplots()
    for key, group in grouped.groupby(COLUMNS[:-1]):
        ax.plot(group[COLUMNS[-1]], group['count'], marker='o')
    
    # Set the x-label and y-label
    x_label = '-'.join(COLUMNS[:-1])
    y_label = COLUMNS[-1]
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    
    return (grouped, ax)