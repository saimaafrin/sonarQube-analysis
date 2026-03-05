
import pandas as pd
import matplotlib.pyplot as plt

def task_func(d, keys=['x', 'y', 'z']):
    # Create a Pandas DataFrame from the list of dictionaries
    df = pd.DataFrame(d)

    # Select the specified keys from the DataFrame
    df = df[keys]

    # Plot the selected keys
    ax = df.plot(kind='line')

    return ax