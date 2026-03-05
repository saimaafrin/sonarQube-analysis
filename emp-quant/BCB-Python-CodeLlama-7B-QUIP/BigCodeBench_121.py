
import pandas as pd
import numpy as np

def task_func(my_list, seed=42):
    if not isinstance(my_list, list):
        raise TypeError("'my_list' must be a list")

    # Generate sales data for different categories
    categories = ['Electronics', 'Fashion', 'Home & Kitchen', 'Automotive', 'Sports']
    sales = pd.DataFrame(np.random.randint(100, size=(5, 5)), columns=categories)

    # Add item "12" to the list
    my_list.append(12)

    # Return the sales data and the bar plot
    return sales, sales.plot.bar()