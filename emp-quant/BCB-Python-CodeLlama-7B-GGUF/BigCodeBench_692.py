
import math
import pandas as pd

def task_func(tuples_list):
    # Create a list of lists, where each inner list contains the sine of each number in the original tuple
    sine_list = [[math.sin(x) for x in tuple] for tuple in tuples_list]
    # Create a DataFrame from the list of lists
    df = pd.DataFrame(sine_list)
    return df