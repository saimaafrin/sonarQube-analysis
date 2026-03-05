import pandas as pd
import random
import matplotlib.pyplot as plt
def task_func(num_rows=100, categories=["a", "b", "c", "d", "e"], random_seed=42):
    if num_rows < 1:
        raise ValueError("num_rows must be at least 1")
    
    random.seed(random_seed)
    data = {'category': random.choices(categories, k=num_rows), 'value': random.randint(1, 100, num_rows)}
    df = pd.DataFrame(data)
    
    # Create a bar chart
    ax = df['category'].value_counts().plot(kind='bar')
    ax.set_title('Category Counts')
    
    return df, ax