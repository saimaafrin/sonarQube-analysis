
import subprocess
import pandas as pd
import matplotlib.pyplot as plt

def task_func(script_path, output_file_path):
    try:
        # Execute the script
        subprocess.run(['python', script_path], check=True)
        
        # Read the CSV file
        df = pd.read_csv(output_file_path)
        
        # Check if the CSV has exactly two columns
        if df.shape[1] != 2:
            raise ValueError("CSV must contain exactly 2 columns")
        
        # Plot the bar graph
        ax = df.plot(kind='bar', x=0, y=1, legend=False)
        
        return df, ax
    except subprocess.CalledProcessError:
        raise ValueError("Script failed to execute")
    except pd.errors.EmptyDataError:
        raise ValueError("CSV is empty")
    except pd.errors.ParserError:
        raise ValueError("CSV is invalid")