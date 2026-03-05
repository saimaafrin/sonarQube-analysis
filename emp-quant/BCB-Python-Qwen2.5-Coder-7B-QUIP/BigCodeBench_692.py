
import math
import pandas as pd

def task_func(tuples_list):
    # Create a list of lists where each sublist contains the sine of the values in the original tuple
    sine_values = [[math.sin(value) for value in tup] for tup in tuples_list]
    
    # Create a DataFrame from the list of sine values
    df = pd.DataFrame(sine_values, columns=[f"sin_{i}" for i in range(len(tuples_list[0]))])
    
    return df