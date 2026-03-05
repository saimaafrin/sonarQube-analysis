
import pandas as pd
import matplotlib.pyplot as plt
from random import randint

def task_func(num_rows=5, rand_range=(0, 100)):
    # Create a DataFrame with random integer values for categories 'A' through 'E'
    data = {chr(65 + i): [randint(rand_range[0], rand_range[1]) for _ in range(num_rows)] for i in range(5)}
    df = pd.DataFrame(data)
    
    # Plot the data with a stacked bar chart
    fig, ax = plt.subplots()
    df.plot(kind='bar', stacked=True, ax=ax)
    
    # Set the title and labels
    ax.set_title('Stacked Bar Chart of Random Integer Values')
    ax.set_xlabel('Categories')
    ax.set_ylabel('Values')
    
    return fig