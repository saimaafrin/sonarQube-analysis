
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(my_list, seed=42):
    if not isinstance(my_list, list):
        raise TypeError("my_list must be a list")
    
    my_list.append("12")
    
    categories = ['Electronics', 'Fashion', 'Home & Kitchen', 'Automotive', 'Sports']
    np.random.seed(seed)
    sales_data = np.random.randint(100, 1000, size=(5,))
    
    df = pd.DataFrame({'Category': categories, 'Sales': sales_data})
    
    fig, ax = plt.subplots()
    df.plot(kind='bar', x='Category', y='Sales', ax=ax)
    ax.set_title('Simulated Sales Data')
    ax.set_xlabel('Categories')
    ax.set_ylabel('Sales')
    
    return df, ax