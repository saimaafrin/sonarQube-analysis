
import pandas as pd
import matplotlib.pyplot as plt
from random import randint

def task_func(num_types=5, integer_range=(0, 100)):
    # Generate random data for each category
    categories = [f'Category {i+1}' for i in range(num_types)]
    data = {category: [randint(integer_range[0], integer_range[1]) for _ in range(num_types)] for category in categories}
    
    # Create a DataFrame
    df = pd.DataFrame(data, index=categories)
    
    # Plotting the horizontal stacked bar chart
    fig, ax = plt.subplots()
    df.plot(kind='barh', stacked=True, ax=ax)
    ax.set_xlabel('Values')
    ax.set_ylabel('Categories')
    ax.set_title('Horizontal Stacked Bar Chart')
    
    return fig, ax