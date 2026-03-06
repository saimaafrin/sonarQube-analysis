
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(data):
    # Convert the input string to a list of integers
    data_list = [int(x.strip()) for x in data.split(',')]
    
    # Create a DataFrame from the list
    df = pd.DataFrame(data_list, columns=['Values'])
    
    # Calculate the bins for the histogram
    bins = np.arange(df['Values'].min(), df['Values'].max() + 2) - 0.5
    
    # Create the histogram
    fig, ax = plt.subplots()
    ax.hist(df['Values'], bins=bins, edgecolor='black')
    
    # Set labels and title
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram of Values')
    
    return ax