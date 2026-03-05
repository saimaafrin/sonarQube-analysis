
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def task_func(num_labels=5, data_range=(0, 1)):
    # Generate random data for each category
    data = np.random.randint(data_range[0], data_range[1], size=(num_labels, num_labels))
    
    # Create a DataFrame to hold the data
    df = pd.DataFrame(data, columns=[f'Label {i+1}' for i in range(num_labels)])
    
    # Plotting the stacked bar chart
    df.plot(kind='bar', stacked=True, figsize=(10, 6))
    plt.title('Stacked Bar Chart of Random Data')
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.legend(title='Labels')
    
    # Return the figure object
    return plt.gcf()