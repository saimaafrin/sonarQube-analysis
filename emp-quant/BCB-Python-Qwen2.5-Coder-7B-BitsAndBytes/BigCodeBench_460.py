
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
        if len(df.columns) != 2:
            raise ValueError("CSV must contain exactly two columns.")
        
        # Plot the bar graph
        fig, ax = plt.subplots()
        ax.bar(df.iloc[:, 0], df.iloc[:, 1])
        ax.set_xlabel(df.columns[0])
        ax.set_ylabel(df.columns[1])
        ax.set_title('Bar Graph from CSV')
        
        return df, ax
    
    except subprocess.CalledProcessError as e:
        raise ValueError(f"Script execution failed with error: {e}")
    
    except FileNotFoundError:
        raise ValueError("Output file not found.")
    
    except pd.errors.EmptyDataError:
        raise ValueError("CSV is empty.")
    
    except Exception as e:
        raise ValueError(f"An unexpected error occurred: {e}")