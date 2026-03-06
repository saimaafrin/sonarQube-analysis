
import numpy as np
import pandas as pd
from pathlib import Path

# Constants
LETTERS = list('abcdefghijklmnopqrstuvwxyz')
OUTPUT_DIR = './output'

def task_func(file_path, output_dir=OUTPUT_DIR):
    # Ensure the output directory exists
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    # Generate a random 2D matrix of lowercase letters
    rows, cols = np.random.randint(1, 101, size=2)  # Random number of rows and columns between 1 and 100
    matrix = np.array([np.random.choice(LETTERS, size=cols) for _ in range(rows)])
    
    # Create a DataFrame from the matrix
    df = pd.DataFrame(matrix)
    
    # Write the DataFrame to a CSV file
    df.to_csv(file_path, header=False, index=False)