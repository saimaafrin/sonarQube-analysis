
import math
import pandas as pd

def task_func(tuples_list):
    # Apply math.sin to each element in the tuples
    transformed_data = [[math.sin(value) for value in tup] for tup in tuples_list]
    # Create a DataFrame from the transformed data
    df = pd.DataFrame(transformed_data)
    return df