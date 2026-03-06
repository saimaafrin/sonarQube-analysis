
import pandas as pd
import numpy as np

def task_func(file_path, num_rows, data_dimensions=5, random_seed=None):
    # Create a Pandas DataFrame with random numeric data
    df = pd.DataFrame(np.random.rand(num_rows, data_dimensions), columns=['Feature_' + str(i) for i in range(1, data_dimensions + 1)])

    # Write the DataFrame to a CSV file
    df.to_csv(file_path, index=False)

    # Return the file path of the generated CSV file
    return file_path