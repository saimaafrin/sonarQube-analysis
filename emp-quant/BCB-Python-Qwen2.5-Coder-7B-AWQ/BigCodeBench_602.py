import numpy as np
import pandas as pd
LETTERS = list('abcdefghijklmnopqrstuvwxyz')
OUTPUT_DIR = './output'
def task_func(file_path, output_dir=OUTPUT_DIR):
    """
    Generates a 2D matrix of random lowercase letters and writes it to a CSV file.

    Parameters:
    file_path (str): The path where the CSV file will be saved.
    output_dir (str): The directory where the output file will be saved. Default is './output'.
    """
    # Ensure the output directory exists
    import os
    os.makedirs(output_dir, exist_ok=True)

    # Generate a random 2D matrix of lowercase letters
    rows, cols = 10, 10  # Example dimensions, can be adjusted
    matrix = np.random.choice(LETTERS, size=(rows, cols))

    # Create a DataFrame from the matrix
    df = pd.DataFrame(matrix)

    # Write the DataFrame to a CSV file
    df.to_csv(file_path, header=False, index=False)