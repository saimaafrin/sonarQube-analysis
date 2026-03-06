
import math
import pandas as pd

def task_func(tuples_list):
    # Convert the list of tuples into a DataFrame
    df = pd.DataFrame(tuples_list)
    
    # Apply math.sin to each element in the DataFrame
    df = df.applymap(math.sin)
    
    return df