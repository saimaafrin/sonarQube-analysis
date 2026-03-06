
import json
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def task_func(json_data: str, key_path: list):
    try:
        # Load JSON data
        data = json.loads(json_data)
        
        # Traverse the JSON using the key path
        current_data = data
        for key in key_path:
            current_data = current_data[key]
        
        # Convert to DataFrame
        df = pd.DataFrame(current_data)
        
        # Filter out non-numeric columns
        numeric_df = df.select_dtypes(include=[np.number])
        
        # Check if there is any numeric data
        if numeric_df.empty:
            raise ValueError("No numeric data found.")
        
        # Create a boxplot
        fig, ax = plt.subplots()
        sns.boxplot(data=numeric_df, ax=ax)
        
        return fig
    
    except KeyError as e:
        raise KeyError(f"Key not found: {e}")
    
    except Exception as e:
        raise ValueError(f"An error occurred: {e}")

key_path = ["data", "records"]

fig = task_func(json_data, key_path)
plt.show()