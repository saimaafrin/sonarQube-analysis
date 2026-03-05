
import pandas as pd
import numpy as np

def task_func(file_path, num_rows, data_dimensions=5, random_seed=None):
    if random_seed is not None:
        np.random.seed(random_seed)
    
    # Generate random data
    data = np.random.rand(num_rows, data_dimensions)
    
    # Create DataFrame
    column_names = [f'Feature_{i+1}' for i in range(data_dimensions)]
    df = pd.DataFrame(data, columns=column_names)
    
    # Save DataFrame to CSV
    df.to_csv(file_path, index=False)
    
    return file_path