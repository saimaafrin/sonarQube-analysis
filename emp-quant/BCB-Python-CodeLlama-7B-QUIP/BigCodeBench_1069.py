
import pandas as pd
import matplotlib.pyplot as plt

def task_func(data_dict):
    # Create a DataFrame from the dictionary
    df = pd.DataFrame(data_dict)

    # Initialize a list to store the histogram Axes objects
    histograms = []

    # Loop through each column in the DataFrame
    for column in df:
        # Generate a histogram for the column
        histogram = df[column].hist(bins=50)

        # Check if the value distribution is uniform
        if not histogram.uniform:
            # Print a message for the non-uniform distribution
            print(f"Column {column} is not uniform")

        # Add the histogram Axes object to the list
        histograms.append(histogram)

    # Return the list of histogram Axes objects
    return histograms