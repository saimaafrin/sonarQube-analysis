
import pandas as pd
import matplotlib.pyplot as plt
from random import randint

def task_func(num_rows=5, rand_range=(0, 100)):
    # Create a DataFrame with random integers
    data = {chr(i): [randint(rand_range[0], rand_range[1]) for _ in range(num_rows)] for i in range(65, 69)}  # A, B, C, D, E
    df = pd.DataFrame(data)
    
    # Plot the DataFrame using a stacked bar chart
    df.plot(kind='bar', stacked=True, figsize=(10, 6))
    plt.title('Stacked Bar Chart of Random Integers')
    plt.xlabel('Index')
    plt.ylabel('Random Integer')
    plt.show()
    
    # Return the figure object
    return plt.figure()