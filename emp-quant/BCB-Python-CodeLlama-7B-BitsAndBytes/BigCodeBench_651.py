
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df, target_value):
    # Convert the input dic of list to a DataFrame
    df = pd.DataFrame(df)

    # Search for rows with cells equal to the provided target_value
    target_rows = df[df == target_value]

    # Count the number of rows with the target value per column
    counts = target_rows.count(axis=0)

    # Create a plot of the counts per column
    fig, ax = plt.subplots()
    ax.bar(counts.index, counts.values)
    ax.set_xlabel('Column')
    ax.set_ylabel('Count')
    ax.set_title('Count of Rows with Target Value')

    return counts, ax