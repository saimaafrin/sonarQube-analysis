
import pandas as pd
import matplotlib.pyplot as plt

def task_func(csv_file_path, col1_name="column1", col2_name="column2"):
    # Read the CSV file
    df = pd.read_csv(csv_file_path)

    # Group the DataFrame by the specified column
    grouped_df = df.groupby(col1_name)

    # Calculate the mean of the specified column for each group
    mean_df = grouped_df[col2_name].mean()

    # Create a bar plot with the mean values
    fig, ax = plt.subplots()
    ax.bar(mean_df.index, mean_df.values, label=col2_name)

    # Set the title and axis labels
    ax.set_title(f"Mean of {col2_name} Grouped by {col1_name}")
    ax.set_xlabel(col1_name)
    ax.set_ylabel(f"Mean of {col2_name}")

    # Return the Axes object
    return ax