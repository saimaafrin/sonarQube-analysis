
import pandas as pd
import numpy as np

def task_func(rows=100, columns=3):
    # Generate a list of column names based on the number of columns
    column_names = [chr(i) for i in range(97, 97 + columns)]
    
    # Create a DataFrame with random alphabets
    data = {col: [chr(np.random.randint(97, 123)) for _ in range(rows)] for col in column_names}
    
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(data)
    
    # Return the DataFrame
    return df