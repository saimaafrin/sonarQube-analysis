
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(my_list, seed=42):
    if not isinstance(my_list, list):
        raise TypeError("'my_list' must be a list")

    np.random.seed(seed)

    categories = ['Electronics', 'Fashion', 'Home & Kitchen', 'Automotive', 'Sports']
    sales_data = pd.DataFrame(np.random.randint(100, size=(5, 5)), columns=categories)

    fig, ax = plt.subplots()
    sales_data.plot(kind='bar', ax=ax)

    return (sales_data, ax)