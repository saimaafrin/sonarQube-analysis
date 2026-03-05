import subprocess
import pandas as pd
import matplotlib.pyplot as plt
def task_func(script_path, output_file_path):
    # Execute the script to produce a CSV file
    subprocess.run(script_path, shell=True, check=True)

    # Read the CSV file into a DataFrame
    df = pd.read_csv(output_file_path)

    # Check that the DataFrame has exactly two columns
    if len(df.columns) != 2:
        raise ValueError("The CSV file does not have exactly two columns.")

    # Plot a bar graph with the first column as the x-axis labels and the second column as the bar heights
    ax = df.plot(kind='bar', x=df.columns[0], y=df.columns[1])

    # Return the DataFrame and the Axes object
    return df, ax
script_path = "script.sh"
output_file_path = "output.csv"