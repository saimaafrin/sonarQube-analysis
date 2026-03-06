
import numpy as np
import pandas as pd

# Constants
LETTERS = list('abcdefghijklmnopqrstuvwxyz')
OUTPUT_DIR = './output'

def task_func(file_path, output_dir=OUTPUT_DIR):
    # Create a 2D matrix with random lowercase letters
    matrix = np.random.choice(LETTERS, size=(10, 10))

    # Convert the matrix to a CSV file
    df = pd.DataFrame(matrix)
    df.to_csv(file_path, index=False)

# Call the function with the desired output file path
task_func('output.csv')