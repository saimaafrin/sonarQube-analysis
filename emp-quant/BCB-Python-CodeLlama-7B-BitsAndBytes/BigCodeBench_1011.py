
import pandas as pd
import matplotlib.pyplot as plt

def task_func(csv_file_path, col1_name="column1", col2_name="column2"):
    # Read the CSV file and create a DataFrame
    df = pd.read_csv(csv_file_path)

    # Group the DataFrame by the specified column and calculate the mean of the other column
    grouped_df = df.groupby(col1_name)[col2_name].mean()

    # Create a bar plot with the mean values for each group
    ax = grouped_df.plot(kind="bar", title=f"Mean of {col2_name} Grouped by {col1_name}")

    # Customize the plot
    ax.set_xlabel(col1_name)
    ax.set_ylabel(f"Mean of {col2_name}")

    return ax

# Show the plot
plt.show()