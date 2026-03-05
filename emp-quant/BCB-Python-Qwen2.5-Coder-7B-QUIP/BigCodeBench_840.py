
import pandas as pd
import numpy as np

def task_func(file_path, num_rows, data_dimensions=5, random_seed=None):
    # Set the random seed if provided
    if random_seed is not None:
        np.random.seed(random_seed)

    # Generate random data
    data = np.random.rand(num_rows, data_dimensions)

    # Create a DataFrame with the generated data
    column_names = [f'Feature_{i}' for i in range(1, data_dimensions + 1)]
    df = pd.DataFrame(data, columns=column_names)

    # Save the DataFrame to a CSV file
    df.to_csv(file_path, index=False)

    # Return the file path of the generated CSV file
    return file_path