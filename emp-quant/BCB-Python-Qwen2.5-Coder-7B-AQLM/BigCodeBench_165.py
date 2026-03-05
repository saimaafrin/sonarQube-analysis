
import pandas as pd
import matplotlib.pyplot as plt
from random import randint

def task_func(num_rows=5, rand_range=(0, 100)):
    # Create a DataFrame with random integer values for categories 'A' through 'E'
    categories = ['A', 'B', 'C', 'D', 'E']
    data = {category: [randint(rand_range[0], rand_range[1]) for _ in range(num_rows)] for category in categories}
    df = pd.DataFrame(data)
    
    # Plot the data using a stacked bar chart
    fig, ax = plt.subplots()
    df.plot(kind='bar', stacked=True, ax=ax)
    ax.set_title('Stacked Bar Chart of Random Integer Values')
    ax.set_xlabel('Index')
    ax.set_ylabel('Values')
    
    return fig