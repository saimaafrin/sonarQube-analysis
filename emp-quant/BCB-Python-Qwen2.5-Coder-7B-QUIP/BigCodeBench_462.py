
import pandas as pd
import random
import matplotlib.pyplot as plt

def task_func(num_rows=100, categories=["a", "b", "c", "d", "e"], random_seed=42):
    if num_rows < 1:
        raise ValueError("num_rows must be at least 1")
    
    # Set the random seed for reproducibility
    random.seed(random_seed)
    
    # Generate random data
    data = {
        'category': [random.choice(categories) for _ in range(num_rows)],
        'value': [random.randint(1, 100) for _ in range(num_rows)]
    }
    
    # Create the DataFrame
    df = pd.DataFrame(data)
    
    # Create the bar chart
    fig, ax = plt.subplots()
    df['category'].value_counts().plot(kind='bar', ax=ax)
    ax.set_title('Category Counts')
    
    return df, ax