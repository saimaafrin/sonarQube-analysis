
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(file_path="data.csv", columns=["A", "B", "C"]):
    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(file_path)

    # Convert the numeric values in the DataFrame to floats
    df = df.apply(pd.to_numeric, errors="coerce")

    # Compute the cube-root of the data
    cube_root = np.cbrt(df[columns])

    # Create a line chart of the data
    fig, ax = plt.subplots()
    ax.plot(df[columns], label="Original Data")
    ax.plot(cube_root, label="Cube Root")
    ax.set_xlabel("Columns")
    ax.set_ylabel("Values")
    ax.legend()

    # Return the DataFrame, Axes, and Series
    return df, ax, cube_root

# Print the DataFrame
print(df)

# Print the Axes
print(ax)

# Print the Series
print(cube_root)