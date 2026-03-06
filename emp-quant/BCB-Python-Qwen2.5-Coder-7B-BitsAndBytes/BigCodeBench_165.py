
import pandas as pd
import matplotlib.pyplot as plt
from random import randint

def task_func(num_rows=5, rand_range=(0, 100)):
    # Create a DataFrame with random integers
    df = pd.DataFrame({
        'A': [randint(rand_range[0], rand_range[1]) for _ in range(num_rows)],
        'B': [randint(rand_range[0], rand_range[1]) for _ in range(num_rows)],
        'C': [randint(rand_range[0], rand_range[1]) for _ in range(num_rows)],
        'D': [randint(rand_range[0], rand_range[1]) for _ in range(num_rows)],
        'E': [randint(rand_range[0], rand_range[1]) for _ in range(num_rows)]
    })

    # Plotting the DataFrame using a stacked bar chart
    fig, ax = plt.subplots()
    df.plot(kind='bar', stacked=True, ax=ax)
    
    # Setting the title and labels
    ax.set_title('Stacked Bar Chart of Random Integers')
    ax.set_xlabel('Index')
    ax.set_ylabel('Values')

    return fig