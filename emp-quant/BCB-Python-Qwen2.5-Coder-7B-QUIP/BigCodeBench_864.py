
import pandas as pd
import numpy as np

def task_func(fruit_data):
    if not fruit_data:
        return pd.DataFrame(columns=['Total Count', 'Average Count'])

    # Create a DataFrame from the input list of tuples
    df = pd.DataFrame(fruit_data, columns=['Fruit', 'Count'])

    # Group the DataFrame by 'Fruit' and calculate the total and average counts
    result = df.groupby('Fruit').agg({'Count': ['sum', 'mean']}).reset_index()

    # Rename the columns for clarity
    result.columns = ['Fruit', 'Total Count', 'Average Count']

    # Set the index to 'Fruit'
    result.set_index('Fruit', inplace=True)

    return result