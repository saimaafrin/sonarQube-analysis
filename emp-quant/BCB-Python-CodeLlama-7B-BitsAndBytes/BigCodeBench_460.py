
import subprocess
import pandas as pd
import matplotlib.pyplot as plt

def task_func(script_path, output_file_path):
    # Execute the script to produce the CSV file
    subprocess.run(script_path, shell=True, check=True)

    # Read the CSV file into a DataFrame
    df = pd.read_csv(output_file_path)

    # Check that the DataFrame has exactly 2 columns
    if len(df.columns) != 2:
        raise ValueError("The produced CSV file does not have exactly 2 columns.")

    # Plot the bar graph
    ax = df.plot(kind='bar', x=df.columns[0], y=df.columns[1])

    # Return the DataFrame and the Axes object
    return df, ax