
import pandas as pd
import matplotlib.pyplot as plt

def task_func(data_dict):
    # Create a Pandas DataFrame from the dictionary
    df = pd.DataFrame(data_dict)

    # Create a list to store the matplotlib Axes objects
    ax_list = []

    # Iterate over the columns of the DataFrame
    for col in df.columns:
        # Generate a histogram for the current column
        ax = df[col].hist(bins=20, alpha=0.5, label=col)
        ax_list.append(ax)

        # Check if the value distribution is uniform
        if not df[col].is_unique:
            print(f"{col} is not uniform")

    # Return the list of matplotlib Axes objects
    return ax_list

ax_list = task_func(data_dict)

# Plot the histograms
for ax in ax_list:
    ax.set_title("Histogram")
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    ax.legend()

plt.show()