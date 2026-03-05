
import subprocess
import pandas as pd
import matplotlib.pyplot as plt

def task_func(script_path, output_file_path):
    try:
        # Execute the script
        subprocess.run([script_path], check=True, text=True)
        
        # Read the CSV file
        df = pd.read_csv(output_file_path, header=None, names=['x', 'y'])
        
        # Check if the CSV has exactly two columns
        if df.shape[1] != 2:
            raise ValueError("CSV must have exactly two columns")
        
        # Plot the bar graph
        ax = df.plot(kind='bar', x='x', y='y', legend=False, ax=plt.subplots()[0])
        
        # Return the DataFrame and the axes object
        return df, ax
    except subprocess.CalledProcessError as e:
        raise ValueError("Script execution failed") from e
    except pd.errors.EmptyDataError as e:
        raise ValueError("CSV is empty") from e
    except pd.errors.ParserError as e:
        raise ValueError("CSV parsing failed") from e