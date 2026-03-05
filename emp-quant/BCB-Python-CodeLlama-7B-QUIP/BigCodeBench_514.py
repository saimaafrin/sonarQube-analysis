
import pandas as pd
import matplotlib.pyplot as plt

def task_func(array):
    # Create a Pandas DataFrame from the 2D list
    df = pd.DataFrame(array, columns=['A', 'B', 'C', 'D', 'E'])

    # Plot the sum of each column
    fig, ax = plt.subplots()
    for col in df.columns:
        ax.plot(df[col].sum())

    return df, ax