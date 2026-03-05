
import numpy as np
import pandas as pd

def task_func(matrix1, matrix2):
    # Convert the matrices to Pandas DataFrames
    df1 = pd.DataFrame(matrix1)
    df2 = pd.DataFrame(matrix2)

    # Concatenate the DataFrames along the columns
    df = pd.concat([df1, df2], axis=1)

    # Convert the DataFrame to a string representation
    str_df = df.to_string(index_names=False, header=False)

    return str_df