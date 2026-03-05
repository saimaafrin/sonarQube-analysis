import pandas as pd
import numpy as np
def task_func(fruit_data):
    if not fruit_data:
        return pd.DataFrame()
    
    # Create a DataFrame from the list of tuples
    df = pd.DataFrame(fruit_data, columns=['Fruit', 'Count'])
    
    # Group by 'Fruit' and calculate total and average counts
    result = df.groupby('Fruit').agg({'Count': ['sum', 'mean']}).reset_index()
    
    # Rename the columns for clarity
    result.columns = ['Fruit', 'Total Count', 'Average Count']
    
    return result.set_index('Fruit')
fruit = [('apple', 1), ('orange', 25), ('apple', 111)]