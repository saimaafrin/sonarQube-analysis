
import numpy as np
import pandas as pd
import os

# Constants
LETTERS = list('abcdefghijklmnopqrstuvwxyz')
OUTPUT_DIR = './output'

def task_func(file_path, output_dir=OUTPUT_DIR):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Generate a random 2D matrix with lowercase letters
    matrix = np.random.choice(LETTERS, size=(10, 10))  # Adjust size as needed

    # Create a DataFrame from the matrix
    df = pd.DataFrame(matrix)

    # Write the DataFrame to a CSV file
    df.to_csv(file_path, index=False, header=False)