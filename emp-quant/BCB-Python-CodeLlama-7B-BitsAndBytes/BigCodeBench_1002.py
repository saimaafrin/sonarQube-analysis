
import pandas as pd
import matplotlib.pyplot as plt

def task_func(data, column_name="target_column"):
    # Check if the specified column exists in the DataFrame
    if column_name not in data.columns:
        raise ValueError(f"Column {column_name} does not exist in the DataFrame")

    # Convert non-numeric columns to categorical type and then to numeric codes
    data = data.apply(pd.to_numeric, errors="coerce")

    # Create a histogram of the specified column
    fig, ax = plt.subplots()
    ax.hist(data[column_name], bins=20, alpha=0.5, label=column_name)
    ax.set_title(f"Histogram of {column_name}")
    ax.set_xlabel(column_name)
    ax.set_ylabel("Frequency")
    ax.legend()

    return data, ax

# Call the function and print the resulting DataFrame and Axes object
data, ax = task_func(data, column_name)
print(data)
print(ax)