import numpy as np
import pandas as pd
LETTERS = list('abcdefghijklmnopqrstuvwxyz')
OUTPUT_DIR = './output'
def task_func(file_path, output_dir=OUTPUT_DIR):
    # Generate a 2D matrix of random lowercase letters
    matrix = np.random.choice(LETTERS, size=(10, 10))
    # Write the matrix to a CSV file
    pd.DataFrame(matrix).to_csv(file_path, index=False)
    return None
file_path = 'output.csv'