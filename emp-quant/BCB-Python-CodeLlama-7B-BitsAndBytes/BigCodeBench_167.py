
import pandas as pd
import matplotlib.pyplot as plt
from random import randint

def task_func(num_types=5, integer_range=(0, 100)):
    # Generate random data
    data = {}
    for i in range(num_types):
        data[f'Type {i}'] = [randint(integer_range[0], integer_range[1]) for _ in range(100)]

    # Create DataFrame
    df = pd.DataFrame(data)

    # Visualize data as a horizontal stacked bar chart
    fig, ax = plt.subplots()
    ax.barh(df.index, df.values, color='#0072B2')
    ax.set_xlabel('Values')
    ax.set_ylabel('Categories')
    ax.set_title('Random Data')
    ax.legend(loc='upper left')
    plt.show()

    return fig, ax

# Call the function and display the plot
fig, ax = task_func(num_types=5, integer_range=(0, 100))