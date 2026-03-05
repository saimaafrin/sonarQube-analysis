import pandas as pd
import numpy as np
def task_func(fruit_data):
    if not fruit_data:
        return pd.DataFrame(columns=['Total Count', 'Average Count'])
    
    # Create a DataFrame from the input list of tuples
    df = pd.DataFrame(fruit_data, columns=['Fruit', 'Count'])
    
    # Group by 'Fruit' and calculate total and average counts
    result_df = df.groupby('Fruit').agg({'Count': ['sum', 'mean']}).reset_index()
    
    # Rename columns for clarity
    result_df.columns = ['Fruit', 'Total Count', 'Average Count']
    
    # Set 'Fruit' as the index
    result_df.set_index('Fruit', inplace=True)
    
    return result_df
fruit = [('apple', 1), ('orange', 25), ('apple', 111)]