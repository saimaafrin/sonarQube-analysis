
import pandas as pd
import random
import matplotlib.pyplot as plt

def task_func(num_rows=100, categories=["a", "b", "c", "d", "e"], random_seed=42):
    if num_rows < 1:
        raise ValueError("num_rows must be at least 1")
    
    # Set the random seed for reproducibility
    random.seed(random_seed)
    
    # Create a list to store the data
    data = []
    
    # Generate random data for each row
    for _ in range(num_rows):
        category = random.choice(categories)
        value = random.randint(1, 100)
        data.append([category, value])
    
    # Create a DataFrame from the data
    df = pd.DataFrame(data, columns=["Category", "Value"])
    
    # Plot the bar chart
    ax = df['Category'].value_counts().plot(kind='bar')
    ax.set_title('Category Counts')
    
    return df, ax