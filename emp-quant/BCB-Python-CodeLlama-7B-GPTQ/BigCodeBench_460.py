import subprocess
import pandas as pd
def task_func(script_path, output_file_path):
    # Execute the script to produce a CSV file
    subprocess.run(script_path, shell=True, stdout=subprocess.PIPE)

    # Read the CSV file into a DataFrame
    df = pd.read_csv(output_file_path)

    # Check that the DataFrame has exactly 2 columns
    if len(df.columns) != 2:
        raise ValueError("The produced CSV file does not have exactly 2 columns.")

    # Plot a bar graph with the first column as the x-axis labels and the second column as the bar heights
    ax = df.plot(kind='bar', x='Column 1', y='Column 2')

    # Return the DataFrame and the Axes object of the plotted bar graph
    return df, ax
script_path = "script.py"
output_file_path = "output.csv"