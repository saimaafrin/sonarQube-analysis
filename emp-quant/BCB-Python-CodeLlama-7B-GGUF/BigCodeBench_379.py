
import pandas as pd
import numpy as np

# Constants
COLUMNS = ['Column1', 'Column2', 'Column3', 'Column4', 'Column5']

def task_func(length):
    # Generate random data
    data = np.random.randint(0, 100, size=(length, len(COLUMNS)))
    # Create a Pandas DataFrame
    df = pd.DataFrame(data, columns=COLUMNS)
    # Print the DataFrame
    print(df)
    # Record the data
    with open('data.csv', 'w') as f:
        df.to_csv(f, index=False)

# Call the function with a specified length
task_func(10)