
import pandas as pd
import matplotlib.pyplot as plt

def task_func(data_dict):
    # Create a DataFrame from the dictionary
    df = pd.DataFrame(data_dict)

    # Create a list to store the histogram Axes objects
    hist_axes = []

    # Iterate over the columns of the DataFrame
    for col in df.columns:
        # Generate a histogram for the current column
        hist_axes.append(df[col].hist(bins=50))

        # Check if the value distribution is uniform
        if not df[col].is_unique:
            print(f"Column {col} has non-uniform distribution")

    # Return the list of histogram Axes objects
    return hist_axes