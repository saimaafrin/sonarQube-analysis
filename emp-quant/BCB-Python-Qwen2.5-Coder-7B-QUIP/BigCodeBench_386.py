
import numpy as np
import pandas as pd
# Constants
COLUMNS = ['Column1', 'Column2', 'Column3', 'Column4', 'Column5']

def task_func(length, min_value=0, max_value=100):
    # Generate a random DataFrame with specified ranges and length
    data = np.random.randint(min_value, max_value, size=(length, len(COLUMNS)))
    df = pd.DataFrame(data, columns=COLUMNS)
    
    # Calculate the cumulative distribution function (CDF)
    cdf = df.apply(lambda x: x.value_counts().cumsum(), axis=0)
    
    # Output the DataFrame
    print("DataFrame:")
    print(df)
    print("\nCDF:")
    print(cdf)
    
    return df, cdf