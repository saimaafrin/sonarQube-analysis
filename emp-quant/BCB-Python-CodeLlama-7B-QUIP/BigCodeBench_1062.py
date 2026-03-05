
import pandas as pd
import matplotlib.pyplot as plt

def task_func(arr):
    # Check if the array is empty
    if arr.size == 0:
        # Create an empty plot with the title 'Time Series of Row Sums'
        fig, ax = plt.subplots()
        ax.set_title("Time Series of Row Sums")
        return ax

    # Compute the sum of elements in each row
    sums = arr.sum(axis=1)

    # Create a Pandas DataFrame with the sums
    df = pd.DataFrame(sums, index=pd.date_range('2020-01-01', periods=len(sums), freq='D'))

    # Plot the DataFrame as a time series
    fig, ax = plt.subplots()
    ax.plot(df)
    ax.set_xlabel("Date")
    ax.set_ylabel("Sum of Rows")
    ax.set_title("Time Series of Row Sums")
    return ax