import pandas as pd
import time
import os
OUTPUT_DIR = './output'
def task_func(df: pd.DataFrame, filename: str) -> str:
    # Ensure the output directory exists
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    # Create a full file path
    file_path = os.path.join(OUTPUT_DIR, filename)
    
    # Write the DataFrame to a JSON Lines file
    df.to_json(file_path, orient='records', lines=True)
    
    # Return the full path where the JSON Lines file was saved
    return file_path