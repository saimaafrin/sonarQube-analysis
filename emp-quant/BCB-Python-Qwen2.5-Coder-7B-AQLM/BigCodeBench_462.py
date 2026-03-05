
import pandas as pd
import random
import matplotlib.pyplot as plt

def task_func(num_rows=100, categories=["a", "b", "c", "d", "e"], random_seed=42):
    if num_rows < 1:
        raise ValueError("num_rows must be at least 1")
    
    random.seed(random_seed)
    data = {
        'Category': [random.choice(categories) for _ in range(num_rows)],
        'Value': [random.randint(1, 100) for _ in range(num_rows)]
    }
    df = pd.DataFrame(data)
    
    category_counts = df['Category'].value_counts()
    bar_chart = category_counts.plot(kind='bar', title='Category Counts')
    
    return df, bar_chart