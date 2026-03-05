
import pandas as pd
import matplotlib.pyplot as plt
from random import randint

def task_func(num_types=5, integer_range=(0, 100)):
    # Generate random data
    categories = [f"Category {i+1}" for i in range(num_types)]
    values = [[randint(integer_range[0], integer_range[1]) for _ in range(num_types)] for _ in range(num_types)]
    df = pd.DataFrame(values, index=categories, columns=categories)
    
    # Plotting the horizontal stacked bar chart
    fig, ax = plt.subplots()
    ax.barh(range(num_types), df.sum(axis=1), height=0.8, edgecolor='black')
    ax.set_yticks(range(num_types))
    ax.set_yticklabels(categories)
    ax.set_xlabel('Values')
    ax.set_title('Horizontal Stacked Bar Chart')
    
    return fig, ax