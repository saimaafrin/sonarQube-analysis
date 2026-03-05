
import json
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def task_func(json_data: str, key_path: list):
    try:
        # Load JSON data
        data = json.loads(json_data)
        
        # Traverse the JSON data using the key path
        for key in key_path:
            data = data[key]
        
        # Convert the data to a pandas DataFrame
        df = pd.DataFrame(data)
        
        # Check if the data contains numeric values
        if not np.issubdtype(df.dtypes[0], np.number):
            raise ValueError("No numeric data found or data is corrupted.")
        
        # Create a boxplot using seaborn
        fig, ax = plt.subplots()
        sns.boxplot(data=df, ax=ax)
        
        return fig
    
    except KeyError as e:
        raise KeyError(f"Key not found: {e}")
    except ValueError as e:
        raise ValueError(f"Error in data: {e}")