
import numpy as np
import pandas as pd
# Constants
LETTERS = list('abcdefghijklmnopqrstuvwxyz')
OUTPUT_DIR = './output'

def task_func(file_path, output_dir=OUTPUT_DIR):
    # Generate a 2D matrix of random lowercase letters
    matrix = np.random.choice(LETTERS, size=(10, 10))  # 10x10 matrix for example

    # Create a DataFrame from the matrix
    df = pd.DataFrame(matrix, columns=[f'col{chr(i)}' for i in range(97, 97+len(matrix[0]))])

    # Write the DataFrame to a CSV file
    df.to_csv(file_path, index=False)

    # Return None to indicate the function has completed
    return None