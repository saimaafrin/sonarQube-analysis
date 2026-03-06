
import pandas as pd
import numpy as np

def task_func(fruit_data):
    if not fruit_data:
        return pd.DataFrame(columns=['Total Count', 'Average Count'])
    
    # Create a DataFrame from the input list of tuples
    df = pd.DataFrame(fruit_data, columns=['Fruit', 'Count'])
    
    # Group by 'Fruit' and calculate the sum and mean of 'Count'
    result_df = df.groupby('Fruit').agg({'Count': ['sum', 'mean']}).reset_index()
    
    # Rename the columns to 'Total Count' and 'Average Count'
    result_df.columns = ['Fruit', 'Total Count', 'Average Count']
    
    # Set the 'Fruit' column as the index
    result_df.set_index('Fruit', inplace=True)
    
    return result_df