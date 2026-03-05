import numpy as np
import pandas as pd
LETTERS = list('abcdefghijklmnopqrstuvwxyz')
OUTPUT_DIR = './output'
def task_func(file_path, output_dir=OUTPUT_DIR):
    """
    Generates a 2D matrix of random lowercase letters and writes it to a CSV file.

    Args:
    file_path (str): The path where the CSV file will be saved.
    output_dir (str): The directory where the output file will be stored.

    Returns:
    None
    """
    # Generate a random 2D matrix of lowercase letters
    matrix = np.random.choice(LETTERS, size=(10, 10))  # 10x10 matrix as an example

    # Create a DataFrame from the matrix
    df = pd.DataFrame(matrix)

    # Write the DataFrame to a CSV file
    df.to_csv(file_path, header=False, index=False)