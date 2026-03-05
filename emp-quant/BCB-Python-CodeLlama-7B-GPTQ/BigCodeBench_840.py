import pandas as pd
import numpy as np
def task_func(file_path, num_rows, data_dimensions=5, random_seed=None):
    """
    Creates a CSV file on a given file path with random numeric data.
    The number of rows in the CSV file is determined by the 'num_rows' parameter,
    and the number of columns (features) is determined by the 'data_dimensions' parameter.
    Columns are named following the convention: 'Feature_x', where x is the number of the feature column starting at 1.
    The function should output with:
        str: The file path of the generated CSV file.
    """
    # Generate random data
    data = np.random.rand(num_rows, data_dimensions)

    # Create a Pandas DataFrame from the data
    df = pd.DataFrame(data, columns=['Feature_' + str(i) for i in range(1, data_dimensions + 1)])

    # Write the DataFrame to a CSV file
    df.to_csv(file_path, index=False)

    # Return the file path of the generated CSV file
    return file_path
file_path = 'data.csv'
num_rows = 100
data_dimensions = 5