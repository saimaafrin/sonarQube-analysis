
import pandas as pd
import time

def task_func(df, target_value):
    # Convert the input dic of list to DataFrame
    df = pd.DataFrame(df)

    # Search for rows with cells equal to the provided target_value
    target_rows = df[df == target_value]

    # Count the number of rows with cells equal to the provided target_value
    count = target_rows.count()

    # Plot the count of rows per column
    fig, ax = plt.subplots()
    ax.bar(df.columns, count)
    ax.set_xlabel("Column")
    ax.set_ylabel("Count")
    ax.set_title("Count of rows with target value")

    return (count, fig)